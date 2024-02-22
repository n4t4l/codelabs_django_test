from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 180)
    content = models.CharField(max_length = 180)
    created_datetime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    username = models.CharField(max_length = 180)

    def __str__(self):
        return self.task
