# Acá hay que registrar todos los modelos armados
# Usuario: mako
# mail: piaggiomaca
#pass: modot

from django.contrib import admin
from .models import Post

#Esto hace al modelo visible en la pagina del administrador
admin.site.register(Post)