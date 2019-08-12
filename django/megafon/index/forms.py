from django.forms import ModelForm
from django import forms
from .models import Author, Books


class BookForm(ModelForm):
    description = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Books
        fields = "__all__"

        def __init__(self, *args, **kargs):
            super(BookForm, self).__init__(*args, **kargs)
            self.fields['author'].label = ''

class AuthorForm(ModelForm):
    description = forms.CharField( widget=forms.TextInput() )
    class Meta:
        model = Author
        fields = "__all__"

        def __init__(self, *args, **kargs):
            super(AuthorForm, self).__init__(*args, **kargs)