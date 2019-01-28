from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""um tópico que o usuário interage"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE,)
	
	def __str__(self):
		"""retorna uma string que representa o modelo"""
		# o método __str__() é chamado para mostrar uma representação
		# simples do Model. nesse caso retornará a string contida na 
		#variável text
		return self.text

class Entry(models.Model):
	"""algo sobre o topico"""
	topic = models.ForeignKey('Topic',on_delete=models.CASCADE,)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		return self.text[:50]+"..."
