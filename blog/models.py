from django.db import models
from django.utils import timezone

# Todo esto va siguiendo el siguiente tutorial:
## https://argentinaenpython.com/django-girls/tutorial/django_models/
# Voy a crear el modelo Post
# Explicacion de modelos: (https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types).
class Post(models.Model):  # class = definir un objeto
	author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
	# ForeignKey marca una relacion con otro modelo.
	# el segundo argumento es para que si borro el post no se borre el autor
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)     
		# Como despues publish() va a updatear published_date,
		# defino los parametros de cuando no hay fecha.

	def publish(self):
		# el argumento "self" refiere al mismo objeto q modifico.
		# esto hace que la funcion pueda acceder a las propiedades del objeto.
		self.published_date = timezone.now()
		# Modifico published_date a la hora ahora. 
		self.save()
		# envío

	# Al llamar __str__() devuelve un string con el titulo
	def __str__(self):
		return self.title
