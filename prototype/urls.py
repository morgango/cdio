from django.urls import path
from prototype import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tables/", views.TablesListView.as_view(), name='tables'),
    path("fields/", views.FieldsListView.as_view(), name='fields'),
    path('fields/create/', views.FieldCreateForm.as_view(), name='field-create'),
    path('fields/<int:pk>/update/', views.FieldUpdateForm.as_view(), name='field-update'),
    path('fields/<int:pk>/delete/', views.FieldDeleteForm.as_view(), name='field-delete'),
]
]