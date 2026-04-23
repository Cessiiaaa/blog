from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)


    class Categorie(models.TextChoices):
        CODING = 'coding', 'Coding'
        CARRIERE = 'carriere', 'Carrière'
        EDUCATION = 'education', 'Éducation'
        TECH = 'tech', 'Tech'
        ENTREPRENEURIAT = 'entrepreneuriat', 'Entrepreneuriat'
        MOTIVATION = 'motivation', 'Motivation'
        OUTILS = 'outils', 'Outils & Ressources'

    categorie = models.CharField(max_length=20, choices=Categorie.choices,)
    description = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)


class CommentModel(models.Model):
    commentaire = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)