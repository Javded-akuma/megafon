from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.functional import curry
from django.db.models import Q

class MainView(View):
    def get(self, request):
        return render(request, 'index.html')

class BookView(View):
    def get(self, request):
        return render(request, 'books.html')

class AuthorsView(View):
    def get(self, request):
        return render(request, 'authors.html')