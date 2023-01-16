# from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic.list import ListView

# for dealing with REST queries
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from django.contrib import messages

# for automatically genenerating Boostrap tables from classes
from django_tables2 import SingleTableView

# for dealing with generic views
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q

# dealing with security
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from guardian.mixins import PermissionRequiredMixin, PermissionListMixin
from guardian.shortcuts import assign_perm, get_objects_for_user, get_perms_for_model

# the data and fields that we are gong to be displaying in the views
from .models import Field, Table
from .tables import TablesTable, FieldsTable 
from .serializers import TableSerializer, UserSerializer
from .forms import TableForm, RegisterUserForm
from django.contrib.auth.forms import UserCreationForm

fields_show = ['name', 'title', 'distribution', 'type', 'subtype', 'format', 'example', 'description'] 
tables_show = ['name', 'description', ] 

# TODO: TableListView, TableDetailView, FieldListView, FieldDetailView 
# https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/

def index(request):
    return render(request, 'index.html')
    
class HomeView(TemplateView):
    template_engine="prototype/index.html"

class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm 
    success_url = reverse_lazy("table-list")
    template_name = "registration/signup.html"


class FieldCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Field
    fields = fields_show
    success_url = reverse_lazy('fields')

    def form_valid (self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)

class FieldUpdateView(PermissionRequiredMixin, UpdateView):
    model = Field
    fields = fields_show 
    success_url = reverse_lazy('fields')

    def form_valid (self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)

class FieldDeleteView(PermissionRequiredMixin, DeleteView):
    model = Field
    success_url = reverse_lazy('fields')

class FieldsListView(PermissionRequiredMixin, SingleTableView):
    model = Field
    table_class = FieldsTable
    template_name = 'prototype/fields.html'

    def get_queryset(self, **kwargs):
         return Field.objects.filter(Q(author=self.request.user.id))

# class TableListView(PermissionRequiredMixin, ListView):
class TableListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Table
    template_name = 'prototype/table_list.html'
    #permission_required = ['view_table', ]
    permission_required = []

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = super(TableListView, self).get_queryset()
            return qs  

        all_model_perms = get_perms_for_model(Table)
        return get_objects_for_user(self.request.user, 'view_table', klass=Table)

class TableDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Table
    permission_required = ['view_table',]

class TableCreateView(LoginRequiredMixin, CreateView):
    model = Table
    form_model = TableForm
    fields = tables_show

    def form_valid(self, form):

        # assign default some values for database integrity
        form.instance.author = self.request.user

        # validate the form for the values that were displayed
        resp = super().form_valid(form)

        # assign object-level permissions for this Table
        assign_perm('view_table', self.request.user, self.object)
        assign_perm('change_table', self.request.user, self.object)
        assign_perm('delete_table', self.request.user, self.object)

        # assign group level permissions for this Table
        customers_grp =  Group.objects.get(name='Customers')
        public_grp =  Group.objects.get(name='Public')
        assign_perm('view_table', customers_grp, self.object)
        assign_perm('view_table', public_grp, self.object)

        return resp

class TableUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Table
    fields = tables_show 
    permission_required = ['view_table', 'change_table']

class TableDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Table
    success_url = reverse_lazy('table-list')
    permission_required = ['view_table', 'delete_table']

# Generating a REST response with all the TABLES
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TableSerializer
    
# Generating a REST response with all the USERS
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
