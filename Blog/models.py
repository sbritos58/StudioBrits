from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now


class Categorias(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de categoría")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-created']


class Post(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to="Post", verbose_name="Imagen", blank=True, null=True)
    publicado = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categorias = models.ManyToManyField(Categorias, verbose_name="Categorias")
    slug = models.SlugField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]


class ContactForm(models.Model):
    nombre_completo = models.CharField(max_length=100, verbose_name="Nombre completo")
    descripcion = models.TextField(verbose_name="Descripción")
    email = models.EmailField(verbose_name="Email")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "ContactForm"
        verbose_name_plural = "ContactForms"
        ordering = ['-created']
