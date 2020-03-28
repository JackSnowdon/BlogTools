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
    path(r'view_account_item/<int:pk>', view_account_item, name="view_account_item"),
    path(r'edit_account_item/<int:pk>', edit_account_item, name="edit_account_item"),
    path(r'delete_account_item/<int:pk>', delete_account_item, name="delete_account_item"),
    path('add_extra_item/', add_extra_item, name="add_extra_item"),
]