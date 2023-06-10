from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")


class Book(models.Model):
    title = models.CharField(max_length=200)
    notes = models.CharField(max_length=10000)
    release_date = models.DateField()
    added = models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    