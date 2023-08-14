from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=90)

