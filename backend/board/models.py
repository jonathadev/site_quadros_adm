from django.db import models

class Note(models.Model):
    text = models.TextField()
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    color = models.CharField(max_length=20, default='yellow')