from django.contrib import admin
from django.urls import path, include

import views

urlpatterns = [
    #path('', views.main, name='main'),
    path('signup', views.RegistrationView.as_view(), name='signup')
]
