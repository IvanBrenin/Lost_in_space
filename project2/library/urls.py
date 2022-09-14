from django.urls import path

from . import views

app_name = 'lib'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('book/all/', view=views.book_list, name='book-list'),
    path('book/<int:pk>/', view=views.book_detail, name='book-detail'),
    path('author/all/', view=views.author_list, name='author-list'),
    path('author/<int:pk>/', view=views.author_detail, name='author-detail'),
    path('genre/all/', view=views.genre_list, name='genre-list'),
    path('book/comment/<int:pk>/', view=views.add_comment, name='add-comment')
]