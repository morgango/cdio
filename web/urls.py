from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from prototype.views import TableViewSet, UserViewSet, TableListView, FieldsListView, TableDetailView, TableCreateView
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
from django.shortcuts import redirect

from tutorial.views import PersonListView
from prototype.views import TableListView
from prototype.views import FieldCreateView, FieldDeleteView, FieldUpdateView
from prototype.views import TableCreateView, TableDeleteView, TableUpdateView
from prototype.views import SignUpView

urlpatterns = [
    path("", views.index, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('tables/', TableListView.as_view(), name='table-list'),
    # path('tables/show=<show>', TableListView.as_view(), name='table-list-body'),
    path('tables/show=<show>', TableListView.as_view(), name='table-list-body'),
    # path('tables/q=<q>', TableListBodyView.as_view(), name='table-list-body'),
    path('<str:author>/tables/', TableListView.as_view(), name='table-list'),
    path('tables/create/', TableCreateView.as_view(), name='table-create'),
    path('<str:author>/tables/create/', TableCreateView.as_view(), name='table-create'),
    path('<str:author>/tables/<slug:slug>/update/', TableUpdateView.as_view(), name='table-update'),
    path('<str:author>/tables/<slug:slug>/delete/', TableDeleteView.as_view(), name='table-delete'),
    path('<str:author>/tables/<slug:slug>/', TableDetailView.as_view(), name='table-slug'),
]