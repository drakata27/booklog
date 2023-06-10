from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'notes', 'release_date', 'added', 'author',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
