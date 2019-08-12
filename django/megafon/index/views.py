from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.functional import curry
from django.db.models import Q
from .models import Author, Books
from .forms import AuthorForm, BookForm

class ListsItem(View):
    template_name = None
    model = None
    form = None
    template_form = None
    redirect_url = None

    def add(self, *args, instance=None, **kwargs):
        # Добавление элемента
        if self.request.method == 'POST':
            form = self.form(self.request.POST,  self.request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/' + kwargs['url'] + '/')
            else:
                return render(self.request, self.template_form)
        else:
            form = self.form()
            content = {
                'form' : form,
                'url' : kwargs['url'],
                'suburl' : kwargs['suburl']
            }
            return render(self.request, self.template_form, content)


    def edit(self, *args, **kwargs):
        # Редактирование элемента при POST запросе
        instance = self.model.objects.get(pk=kwargs['pk'])
        if self.request.method == 'POST':
            form = self.form(self.request.POST, self.request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/' + kwargs['url'] + '/')
        else:
            print(kwargs)
            form = self.form(instance=instance)
            content = {
                'pk' : kwargs['pk'],
                'form' : form
            }
            return render(self.request, self.template_form, content)

        # Удаление элемента GET
    def delete(self, *args, **kwargs):
        model = self.model
        pass

    def get(self, request, url='', suburl='', pk=''):
        # Перенаправляем запросы GET
        if suburl == 'add':
            return self.add(request, url=url, suburl=suburl, pk=pk)
        if suburl == 'edit':
            return self.edit(request, url=url, suburl=suburl, pk=pk)
        if suburl == 'del':
            return self.delete(request, url=url, suburl=suburl, pk=pk)

        if 'search' in request.GET:
            # Поиск по спискам
            print('search')
            return HttpResponse('search')
        else:
            items = self.model.objects.all()
            content = {
                'items' : items,
                'url_list' : url,
                'suburl' : suburl,
            }
            return render(request, self.template_name, content)

    def post(self, request, url='', suburl='', pk=''):
        # Перенаправляем запросы POST
        if suburl == 'add':
            return self.add(request, url=url, suburl=suburl, pk=pk)
        if suburl == 'edit':
            return self.edit(request, url=url, suburl=suburl, pk=pk)

class MainView(View):
    def get(self, request):
        return render(request, 'index.html')

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