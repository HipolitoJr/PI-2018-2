from django.db import models

# Create your models here.

class Resultado(models.Model):

    url = models.CharField('Url', max_length=255, blank=False, null=False)
    resultado = models.TextField('Resultado', max_length=255, blank=False, null=False)