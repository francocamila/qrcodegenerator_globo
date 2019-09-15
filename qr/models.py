from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    url = models.TextField()
    time = models.DateField(auto_now = True)
    category = models.TextField()

#    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.url

class Expense(models.Model):
    category = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.category