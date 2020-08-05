from django.db import models

class AdminModel(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)

	def __str__(self):
		return self.username +" | "+ self.password

class PizzaModel(models.Model):
	name = models.CharField(max_length = 20)
	price = models.CharField(max_length = 20)

	def __str__(self):
		return self.name +" | "+ self.price