from django.urls import path
from prototype import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("tables/", views.tables, name="tables"),
    path("tables/", views.TablesListView.as_view(), name='tables'),
]