from django.db import models
from accounts.models import Profile

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    done_by = models.ForeignKey(Profile, related_name='tasks', on_delete=models.PROTECT)

    def __str__(self):
        return self.task


class AccountItem(models.Model):
    item = models.CharField(max_length=255)
    done_by = models.ForeignKey(Profile, related_name='items', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    expense = models.BooleanField(default=False)
    amount = models.IntegerField()

    def __str__(self):
        return self.item