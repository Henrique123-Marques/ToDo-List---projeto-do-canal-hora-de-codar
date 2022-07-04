from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Tarefa(models.Model):

	STATUS = (
		('fazendo', 'Fazendo',),
		('feito', 'Feito'),
	)

	titulo = models.CharField(max_length= 255)
	descricao = models.TextField()
	feito = models.CharField(
		max_length = 10,
		choices = STATUS,
		)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	criado = models.DateTimeField(auto_now_add=True)
	atualizado = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.titulo