from django.db import models
from django.urls import reverse
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=128)
    # books

    def __str__(self):
        return self.name

    def url(self):
        return reverse('lib:genre-list') + f'#g-{self.id}'



class Author(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    portrait = models.URLField(null=True, blank=True)
    # books

    def __str__(self):
        return f'{self.first} {self.last}'

    def url(self):
        return reverse('lib:author-detail', kwargs={'pk': self.id})

    def genres(self):
        # genre_list = []
        # for book in self.books.all():
        #     for genre in book.genres.all():
        #         if genre not in genre_list:
        #             genre_list.append(genre)
        genre_list = Genre.objects.filter(books__author__exact=self).distinct()
        return genre_list

    def comments(self):
        return Comment.objects.filter(book__author__exact=self)


class Book(models.Model):
    title = models.CharField(max_length=512)
    cover = models.URLField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)
    # comments
    # instances

    def __str__(self):
        return f'"{self.title}"'

    def url(self):
        return reverse('lib:book-detail', kwargs={'pk': self.id})


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published']


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='instances')
    LOAN_STATUSES = (
        ('a', 'available'),
        ('o', 'on loan'),
        ('m', 'maintenance'),
        ('r', 'reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUSES,
                              default='a')

    due_back = models.DateField(null=True, blank=True)


    # def __str__(self):
    #     return f'"{self.title}"'