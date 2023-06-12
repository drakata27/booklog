from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BooksListView.as_view(), name='books_list'),
    path('books/add', views.BooksCreateView.as_view(), name='books_add'),
    path('books/<int:pk>', views.BooksDetailView.as_view(), name='books_detail'),
    path('books/<int:pk>/edit', views.BooksUpdateView.as_view(), name='books_edit'),
    path('books/<int:pk>/delete', views.BooksDeleteView.as_view(), name='books_delete'),
]