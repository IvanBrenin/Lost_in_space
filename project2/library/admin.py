from django.contrib import admin

from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last', 'first']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'book']
    list_filter = ['author', 'book', 'published']

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass