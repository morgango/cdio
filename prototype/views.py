# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic.list import ListView

# the base classes we care about
from .models import Table, Field

# for dealing with REST queries
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import TableSerializer, UserSerializer

# for automatically genenerating Boostrap tables from classes
from django_tables2 import SingleTableView
from .tables import TablesTable, FieldsTable 


# def index(request):
#     return render(request, 'prototype/table_list.html')

# def home(request):
#     return HttpResponse("Hello, Django!")

# Generating a list of all the fields

# for dealing with generic views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Field, Table

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

@method_decorator(login_required, name='dispatch')
class FieldCreateForm(CreateView):
    model = Field
    fields = '__all__'
    success_url = reverse_lazy('fields')
    #success_url = '/fields/'

class FieldUpdateForm(UpdateView):
    model = Field
    fields = '__all__'
    success_url = reverse_lazy('fields')
    #success_url = '/fields/'

class FieldDeleteForm(DeleteView):
    model = Field
    success_url = reverse_lazy('fields')

class TableCreateForm(CreateView):
    model = Table
    fields = '__all__'
    success_url = '/tables/'

class TableUpdateForm(UpdateView):
    model = Table
    fields = '__all__'
    success_url = '/tables/'

class TableDeleteForm(DeleteView):
    model = Table
    success_url = reverse_lazy('tables')

# Generating a list of all the FIELDS
class FieldsListView(SingleTableView):
    model = Field
    table_class = FieldsTable
    template_name = 'prototype/fields.html'

# Generating a list of all the TABLES
class TablesListView(SingleTableView):
    #model = Table
    table_class = TablesTable
    template_name = 'prototype/tables.html'
    #queryset = Table.objects.all()
    d = super().get_context_data()
    queryset = Table.objects.filter(author=2)

# Generating a REST response with all the TABLES
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TableSerializer
    
# Generating a REST response with all the USERS
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
