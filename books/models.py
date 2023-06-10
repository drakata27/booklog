from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    notes = models.CharField(max_length=10000)
    release_date = models.DateField()
    added = models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book")

    