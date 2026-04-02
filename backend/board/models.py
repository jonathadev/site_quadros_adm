from django.db import models

class Note(models.Model):
    text = models.TextField(default="Novo Post-it")
    color = models.CharField(max_length=20, default="yellow")
    area = models.CharField(max_length=50, default="desafios")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.area} - {self.order}"