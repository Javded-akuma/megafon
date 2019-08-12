from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.functional import curry
from django.db.models import Q
from .models import Author, Books
from .forms import AuthorForm, BookForm
from .utils import ListsItem


class MainView(View):
    def get(self, request, url='', suburl='', pk=''):
        books = Books.objects.all()
        author = Author.objects.all()
        content = {
            'books' : books,
            'author' : author
        }
        return render(self.request, 'index.html', content)

class BookView(ListsItem):
    # Наследуем класс ListsItem для книг
    template_name = 'books.html'
    model = Books
    form = BookForm
    template_form = 'book.html'

class AuthorsView(ListsItem):
    # Наследуем класс ListsItem для авторов
    template_name = 'authors.html'
    model = Author
    form = AuthorForm
    template_form = 'author.html'