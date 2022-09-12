from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *


def index(request):
    context = {
        'books_number': len(Book.objects.all()),
        'authors_number': len(Author.objects.all()),
        'genres_number': len(Genre.objects.all()),
    }
    return render(request, template_name='library/index.html', context=context)


def book_list(request):
    context = {
        'books': Book.objects.order_by('title'),
    }
    return render(request, template_name='library/book_list.html', context=context)


def book_detail(request, pk):
    context = {
        'book': Book.objects.get(pk=pk),
    }
    return render(request, template_name='library/book_detail.html', context=context)


def author_list(request):
    context = {
        'authors': Author.objects.order_by('last', 'first'),
    }
    return render(request, template_name='library/author_list.html', context=context)


def author_detail(request, pk):
    context = {
        'author': Author.objects.get(id__exact=pk),
    }
    return render(request, template_name='library/author_detail.html', context=context)


def genre_list(request):
    context = {
        'genres': Genre.objects.order_by('name'),
    }
    return render(request, template_name='library/genre_list.html', context=context)


def add_comment(request, pk):
    text = request.POST.get('text')
    author = request.POST.get('author')
    book = get_object_or_404(Book, id=pk)
    if text and author:
        new_comment = Comment(text=text, author=author, book=book)
        new_comment.save()
    return HttpResponseRedirect(book.url())