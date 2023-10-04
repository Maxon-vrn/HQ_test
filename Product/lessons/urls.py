from django.contrib.auth import logout
from django.urls import path
from django.views.defaults import page_not_found

from .views import *

urlpatterns = [
    path('', index, name='index'),


    ]
