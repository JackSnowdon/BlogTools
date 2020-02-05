from django.urls import path
from .views import *

urlpatterns = [
    path('toolshome/', toolshome, name="toolshome"),
]