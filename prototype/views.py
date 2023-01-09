# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic.list import ListView

# for dealing with REST queries
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

# for automatically genenerating Boostrap tables from classes
from django_tables2 import SingleTableView

# for dealing with generic views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q

# dealing with security
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

# the data and fields that we are gong to be displaying in the views
from .models import Field, Table
from .tables import TablesTable, FieldsTable 
from .serializers import TableSerializer, UserSerializer

fields_show = ['name', 'title', 'distribution', 'type', 'subtype', 'format', 'example', 'description'] 
tables_show = ['name', 'description',] 

# TODO: TableListView, TableDetailView, FieldListView, FieldDetailView 
# Add is_visible to each of the models.
# https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/

class TableListView(ListView):
     model = Table
     template_name = 'prototype/table_list.html'
     ordering = ['slug']
     
     def get_context_data(self, **kwargs):
         return super().get_context_data(**kwargs)

     def get_queryset(self):
        if self.request.user.is_authenticated:
            # return Table.objects.filter(Q(author=self.request.user.id)) 
            return Table.objects.filter(visibility>0, user=self.request.user)
        else:
            return Table.objects.none()

# @method_decorator(login_required, name='dispatch')
class FieldCreateForm(LoginRequiredMixin, CreateView):
    model = Field
    fields = fields_show
    success_url = reverse_lazy('fields')

    def form_valid (self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)

class FieldUpdateForm(LoginRequiredMixin, UpdateView):
    model = Field
    fields = fields_show 
    success_url = reverse_lazy('fields')

    def form_valid (self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)

class FieldDeleteForm(LoginRequiredMixin, DeleteView):
    model = Field
    success_url = reverse_lazy('fields')

# Generating a list of all the FIELDS
class FieldsListView(LoginRequiredMixin, SingleTableView):
    model = Field
    table_class = FieldsTable
    template_name = 'prototype/fields.html'

    def get_queryset(self, **kwargs):
         return Field.objects.filter(Q(author=self.request.user.id))

class TableCreateForm(LoginRequiredMixin, CreateView):
    model = Table
    fields = tables_show 
    success_url = '/tables/'

    def form_valid (self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)

class TableUpdateForm(LoginRequiredMixin, UpdateView):
    model = Table
    fields = tables_show 
    success_url = '/tables/'

    def form_valid (self, form):
        form.instance.author_id = self.request.user.id
        form.save()
        return super().form_valid(form)

class TableDeleteForm(LoginRequiredMixin, DeleteView):
    model = Table
    success_url = reverse_lazy('tables')

# Generating a list of all the TABLES
class TablesListView(LoginRequiredMixin, SingleTableView):
    model = Table
    table_class = TablesTable
    template_name = 'prototype/tables.html'

    def get_queryset(self, **kwargs):

        queryset = Table.objects.filter(Q(author=self.request.user.id))
        return queryset

# Generating a REST response with all the TABLES
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TableSerializer
    
# Generating a REST response with all the USERS
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
