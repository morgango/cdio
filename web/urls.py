from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from prototype.views import TableListView, FieldsListView, TableDetailView, TableCreateView, TableLikeView, TableCommentView, TableFollowerView, TableRatingView
from prototype.serializers import UserSerializer, TableSerializer
from prototype import views
import prototype 

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
    path('tables/show=<show>', TableListView.as_view(), name='table-list-body'),
    path('<str:author>/tables/', TableListView.as_view(), name='table-list'),
    path('tables/create/', TableCreateView.as_view(), name='table-create'),
    path('<str:author>/tables/create/', TableCreateView.as_view(), name='table-create'),
    path('<str:author>/tables/<slug:slug>/update/', TableUpdateView.as_view(), name='table-update'),
    path('<str:author>/tables/<slug:slug>/delete/', TableDeleteView.as_view(), name='table-delete'),
    path('<str:author>/tables/<slug:slug>/', TableDetailView.as_view(), name='table-slug'),
    path('<str:author>/tables/<slug:slug>/like', TableLikeView.as_view(), name='table-like'),
    path('<str:author>/tables/<slug:slug>/rating', TableRatingView.as_view(), name='table-rating'),
    path('<str:author>/tables/<slug:slug>/comment', TableCommentView.as_view(), name='table-comment'),
    path('<str:author>/tables/<slug:slug>/follow', TableFollowerView.as_view(), name='table-follow'),
]