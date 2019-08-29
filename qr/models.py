from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    URL = models.TextField()
#    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.URL