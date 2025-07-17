from django.contrib import admin
from .models import Post, Comentario  # Importa los modelos que quieres registrar en el admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Comentario)