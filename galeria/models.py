from django.db import models

class Cuadro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descipcion = models.TextField()
    imagen = models.ImageField(upload_to='cuadros/')

class Escultura(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descipcion = models.TextField()
    imagen = models.ImageField(upload_to='esculturas/')

class Ceramica(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descipcion = models.TextField()
    imagen = models.ImageField(upload_to='ceramicas/')