from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=100, label="Author", widget=forms.TextInput(attrs={'class': 'form-control'}))
    genre = forms.CharField(max_length=50, label="Genre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.IntegerField(label="Publication Year", widget=forms.NumberInput(attrs={'class': 'form-control'}))
