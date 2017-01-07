from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)


class Question(models.Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    quiz = models.ForeignKey(Quiz)


class Answer(models.Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    score = models.IntegerField(null=True)
    is_correct = models.NullBooleanField()


class UserAnswer(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
