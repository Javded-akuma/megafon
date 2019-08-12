from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    # path('/', views.MainView.as_view(), name='index'),
    url(r'^(?P<url>books)/$', views.BookView.as_view(), name='books'),
    url(r'^(?P<url>books)\/(?P<suburl>add)/$', views.BookView.as_view(), name='books_add'),
    url(r'^(?P<url>books)\/(?P<suburl>edit)\/(?P<pk>\d+)', views.BookView.as_view(), name='books_edit'),
    url(r'^(?P<url>books)\/(?P<suburl>del)\/(?P<pk>\d+)', views.BookView.as_view(), name='books_del'),

    url(r'^(?P<url>authors)/$', views.AuthorsView.as_view(), name='authors'),
    url(r'^(?P<url>authors)\/(?P<suburl>add)/$', views.AuthorsView.as_view(), name='authors_add'),
    url(r'^(?P<url>authors)\/(?P<suburl>edit)\/(?P<pk>\d+)', views.AuthorsView.as_view(), name='authors_edit'),
    url(r'^(?P<url>authors)\/(?P<suburl>del)\/(?P<pk>\d+)', views.AuthorsView.as_view(), name='authors_del'),
]