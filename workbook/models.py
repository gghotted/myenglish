from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    mean = models.TextField()
    is_saved = models.BooleanField(default=False)


class Recode(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('wtm', 'wtm'), ('mtw', 'mtw')])
    hit = models.BooleanField()