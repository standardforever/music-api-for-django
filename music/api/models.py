from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.email


class Album(models.Model):
    artist = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

class MusicGenre(models.Model):
    name = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)

class MusicGenreQuiz(models.Model):
    music_genre = models.ForeignKey(MusicGenre, on_delete=models.CASCADE, related_name='quiz')
    option_1 = models.CharField(max_length=250)
    option_2 = models.CharField(max_length=250)
    option_3 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    question_id = models.IntegerField()
    question = models.CharField(max_length=250)

