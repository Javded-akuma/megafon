from django.forms import ModelForm
from django import forms
from .models import Author, Books


class BookForm(ModelForm):
    # Переопределяем поле description
    description = forms.CharField( widget=forms.Textarea )
    class Meta:
        # Берем все поля из базы
        model = Books
        fields = "__all__"

    def __init__(self, *args, **kargs):
        super(BookForm, self).__init__(*args, **kargs)
        # Изменяем лейблы полей формы
        self.fields['author'].label = 'Авторы'
        self.fields['description'].label = 'Описание'
        self.fields['image'].label = 'Изображение'

class AuthorForm(ModelForm):
    # Переопределяем поле description
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        # Берем все поля из базы
        model = Author
        fields = "__all__"

    def __init__(self, *args, **kargs):
        super(AuthorForm, self).__init__(*args, **kargs)
        # Изменяем лейблы полей формы
        self.fields['description'].label = 'Описание'
        self.fields['image'].label = 'Изображение'