from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'notes', 'release_date', 'added', 'author',)

admin.site.register(models.Book, BookAdmin)
