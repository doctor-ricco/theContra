from django.urls import path, include
from django.contrib import admin

import account.views

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', account.views.home, name = 'home'),
]