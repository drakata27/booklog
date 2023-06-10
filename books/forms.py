from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'notes', 'release_date', 'added', 'author')
        widgets = {}

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name')
        widgets = {
            'name':  forms.TextInput(attrs={'class': 'form-control my-5'}),
        }