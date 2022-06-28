from django import forms
from main.models import Director, Movie

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name'.split()
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи имя режиссера'
            })
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title description director'.split()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи название фильма'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'заполните описание фильма'
            }),
            'director': forms.Select(attrs={
                'class': 'form-control'
            })
        }
