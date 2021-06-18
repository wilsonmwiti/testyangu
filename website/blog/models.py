from datetime import date
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Post(models.Model):
    category = models.CharField(max_length=40,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateField(default=date.today)
    claps = models.IntegerField(default=0)
    image=models.ImageField(upload_to="website/blog",blank=True)
    
    def __str__(self):
        return self.title
