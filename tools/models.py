from django.db import models
from accounts.models import Profile

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    done_by = models.ForeignKey(Profile, related_name='tasks', on_delete=models.PROTECT)

    def __str__(self):
        return self.task