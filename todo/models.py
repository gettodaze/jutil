from django.db import models


class TodoTask(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)


# Create your models here.
