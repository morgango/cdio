from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from prototype.views import TableViewSet, UserViewSet, TablesListView, FieldsListView
from prototype.serializers import UserSerializer, TableSerializer
from prototype import views
import prototype 

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', TableViewSet)

# urlpatterns = [
#     #path("", include("prototype.urls")),
#     #path("tables/", include("prototype.urls")),
#     re_path('$', views.index, name='tables'),
#     path("api/", include(router.urls)),
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls'))
# ]

from django.urls import path
from django.contrib import admin

from tutorial.views import PersonListView
from prototype.views import FieldCreateForm, FieldDeleteForm, FieldUpdateForm
from prototype.views import TableCreateForm, TableDeleteForm, TableUpdateForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("people/", PersonListView.as_view()),
    path("fields/", FieldsListView.as_view(), name='fields'),
    path('fields/create/', FieldCreateForm.as_view(), name='field-create'),
    path('fields/<int:pk>/update/', FieldUpdateForm.as_view(), name='field-update'),
    path('fields/<int:pk>/delete/', FieldDeleteForm.as_view(), name='field-delete'),
    path("tables/", TablesListView.as_view(), name='tables'),
    path('tables/create/', TableCreateForm.as_view(), name='table-create'),
    path('tables/<int:pk>/update/', TableUpdateForm.as_view(), name='table-update'),
    path('tables/<int:pk>/delete/', TableDeleteForm.as_view(), name='table-delete'),
]