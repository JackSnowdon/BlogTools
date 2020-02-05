from django.urls import path
from .views import *

urlpatterns = [
    path('toolshome/', toolshome, name="toolshome"),
    path('checklist/', checklist, name="checklist"),
    path('add_checklist/', add_checklist, name="add_checklist"),
    path(r'edit_checklist/<int:pk>', edit_checklist, name="edit_checklist"),
]