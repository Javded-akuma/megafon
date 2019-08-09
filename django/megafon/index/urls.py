from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    # path('/', views.MainView.as_view(), name='index'),
    url(r'^books/$', views.BookView.as_view(), name='books'),
    url(r'^authors/$', views.AuthorsView.as_view(), name='authors'),
]