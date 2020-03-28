from django import forms
from .models import *

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = ["completed", "done_by"]


class AccountForm(forms.ModelForm):

    class Meta:
        model = AccountItem
        exclude = ["created_on", "done_by"]


class ExtraItemForm(forms.ModelForm):

     class Meta:
        model = ExtraItem
        exclude = ["created_on", "done_by"]