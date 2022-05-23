from django.db import models

class Certif(models.Model):
    title = models.CharField(max_length=200, 
        verbose_name="Título")
    description = models.TextField(
        verbose_name="Descripción")
    image = models.ImageField(upload_to="certifs",  
        verbose_name="Imagen")
    link = models.URLField(null=True, blank=True,  # <=====
        verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "certificado"
        verbose_name_plural = "certificados"
        ordering = ["-created"]

    def __str__(self):
        return self.title