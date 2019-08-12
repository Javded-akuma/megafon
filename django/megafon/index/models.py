from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(_("Имя автора"), max_length=200)
    last_name = models.CharField(_("Фамилия автора"), max_length=200)
    description = models.CharField(_("Описание автора"), max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='static/img/', blank=True, null=True) 

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    objects = models.Manager()

class Books(models.Model):
    name = models.CharField(_("Название книги"), max_length=200)
    author = models.ManyToManyField(Author, blank=True)
    description = models.CharField(_("Описание книги"), max_length=2000, blank=True, null=True)
    series = models.CharField(_("Серия"), max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='static/img/', blank=True, null=True) 

    def __str__(self):
        return self.name
    objects = models.Manager()