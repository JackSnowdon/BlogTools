from django.urls import path
from .views import *

urlpatterns = [
    path('toolshome/', toolshome, name="toolshome"),
    path('checklist/', checklist, name="checklist"),
    path('add_checklist/', add_checklist, name="add_checklist"),
    path(r'edit_checklist/<int:pk>', edit_checklist, name="edit_checklist"),
    path(r'delete_task/<int:pk>', delete_task, name="delete_task"),
    path(r'complete_task/<int:pk>', complete_task, name="complete_task"),
    path('account/', account, name="account"),
    path('add_account_item/', add_account_item, name="add_account_item"),
]