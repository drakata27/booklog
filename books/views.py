from django.views.generic import CreateView,DetailView, ListView, UpdateView
from .models import Book
from .forms import BookForm
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Books Views
class BooksDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = '/books'
    login_url = '/login'


class BooksUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    form_class = BookForm
    success_url = '/books'
    login_url = '/login'

class BooksDetailView(LoginRequiredMixin,DetailView):
    model = Book
    context_object_name = 'book'
    login_url = '/login'

class BooksCreateView(LoginRequiredMixin,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = '/books'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)

class BooksListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.book.all()
