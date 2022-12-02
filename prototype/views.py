from django.http import HttpResponse
from django.shortcuts import render
from .models import Table
from django.views.generic.list import ListView

def home(request):
    return HttpResponse("Hello, Django!")

class TablesListView(ListView):
    # model = Table
    # ordering = ['name']
    # TODO: Add a .filter to the .objects to restrict by owner
    queryset = Table.objects.order_by('name')[:10]