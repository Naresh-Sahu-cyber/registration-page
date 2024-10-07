from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    
    path('home/',user_home),
    path("user-data/",user_data),
    path("delete-user/<int:user_id>",delete_user),
]