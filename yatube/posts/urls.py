from tokenize import group
from django.urls import path
from . import views

from. import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
]
