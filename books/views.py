from django.views.generic import CreateView,DetailView, ListView, UpdateView
from .models import Book
from .forms import BookForm
from django.http.response import HttpResponseRedirect

# Books Views
class BooksCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_add.html'
    success_url = '/books'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)

class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
