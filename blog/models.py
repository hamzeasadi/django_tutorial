from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse

class Post(models.Model):
    """post model for creating posts by users"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, default='None', on_delete=models.CASCADE)
    date_posted = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')
