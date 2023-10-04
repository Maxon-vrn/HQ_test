"""
URL configuration for Product project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from lessons.views import *   # impot all views functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),   #index-start page
    path('statistic/', statistic, name='statistic'),
    path('contact/', contact, name='contact'),
    path('captcha/', include('captcha.urls')),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('registration', RegisterUser.as_view(), name='registration'),
    path('lessons/<int:lessons_id>/', show_lessons, name='lessons'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
