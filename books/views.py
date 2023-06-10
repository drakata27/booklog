from django.views.generic import CreateView,DetailView, ListView, UpdateView
from .models import Author, Book

# Books Views
class BooksListView(ListView):
    model = Book
    #check
    context_object_name = 'books'
    template_name = 'books/books_list.html'