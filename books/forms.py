from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author', 'notes', 'release_date',)
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control mb5'})
        }