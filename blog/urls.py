from django.conf.urls import url
from . import views    # Importa todas las vistas de la app blog

urlpatterns = [
    # Si entra con (link), esta es la pagina a mostrar
    url(r'^$', views.post_list, name='post_list'), # name es el nombre de la url, NO la url

]