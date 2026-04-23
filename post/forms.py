from django import forms
from .models import Post, CommentModel, User
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titre', 'auteur','categorie', 'description', 'contenu']
        widgets = {
            'contenu': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['commentaire']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
