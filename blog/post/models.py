from django.db import models
import uuid 

# Create your models here.

class Post (models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField() #Descripcion de la sección de emprendimientos
    imagen_seccion = models.ImageField(null=True, blank=True, default= "default_image.png")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


def __str__(self):
    return self.titulo

