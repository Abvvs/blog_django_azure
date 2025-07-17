from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):    # de tipo una a muchas
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.post.titulo}'

#class Etiquetas(models.Model):     #de tipo muchas a muchas la etiqueta puede tener muchos posts y un post puede tener muchas etiquetas

""" 
BooleanField is a field for storing True/False values.
IntegerField is a field for storing integer values.
EmailField is a field for storing email addresses.
CharField is a field for storing short text strings.
DateField is a field for storing date values.
DateTimeField is a field for storing date and time values.
TextField is a field for storing long text strings.
ForeignKey is a field for creating a many-to-one relationship with another model.
ManyToManyField is a field for creating a many-to-many relationship with another model.

"""

""" 
DESPUES DE CREAR EL MODELO, EJECUTAR:
python manage.py makemigrations # ESTO PREPARA LOS ARCHIVOS DE MIGRACION
python manage.py migrate # ESTO CREA LA TABLA EN LA BASE DE DATOS, APLICA LOS CAMBIOS EN LA BASE DE DATOS
# Para crear un superusuario y poder acceder al admin:
"""