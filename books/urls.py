from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BooksListView.as_view(), name='books_list'),
    path('books/add', views.BooksCreateView.as_view(), name='books_add'),
]