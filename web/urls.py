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
from prototype.views import TableListView
from prototype.views import FieldCreateForm, FieldDeleteForm, FieldUpdateForm
from prototype.views import TableCreateForm, TableDeleteForm, TableUpdateForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("people/", PersonListView.as_view()),
    path("<str:author>/fields/", FieldsListView.as_view(), name='fields'),
    path('<str:author>/fields/create/', FieldCreateForm.as_view(), name='field-create'),
    path('<str:author>/fields/<slug:slug>/update/', FieldUpdateForm.as_view(), name='field-update'),
    path('<str:author>/fields/<slug:slug>/delete/', FieldDeleteForm.as_view(), name='field-delete'),
    path('<str:author>/tables/<slug:slug>/', FieldsListView.as_view(), name='field-slug'),
    # We will need this when we have a field detail view
    # path('<str:author>/fields/<int:id>/', XXXXXXXXXXXX_View.as_view(), name='field-id'),
    path("<str:username>/tables/", TablesListView.as_view(), name='tables'),
    path('<str:author>/tables/create/', TableCreateForm.as_view(), name='table-create'),
    path('<str:author>/tables/<slug:slug>/update/', TableUpdateForm.as_view(), name='table-update'),
    path('<str:author>/tables/<slug:slug>/delete/', TableDeleteForm.as_view(), name='table-delete'),
    path('<str:author>/tables/<int:id>/', FieldsListView.as_view(), name='field-id'),
    path('tables/', TableListView.as_view(), name='table-list'),
]