# blog/forms.py
from django import forms
from .models import Post
from .models import CustomUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Este es el espacio para el titulo'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Este es el espacio para el titulo'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AvatarForm(forms.ModelForm):
    AVATAR_CHOICES = [
        ('avatar.jpg', 'Avatar 1'),
        ('lord.jpg', 'Avatar 2'),
        ('potter.jpg', 'Avatar 3'),
        ('starwars.jpg', 'Avatar 4'),
    ]

    avatar = forms.ChoiceField(choices=AVATAR_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['avatar']