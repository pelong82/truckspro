from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Tire(models.Model):
	measure = models.CharField(max_length=30)
	brand = models.CharField(max_length=40)
	serie = models.CharField(max_length=30)
	design = models.CharField(max_length=30)


class Address(models.Model):
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=60, default='Baja California')
	street = models.CharField(max_length=60)
	number = models.IntegerField()
	zip_code = models.IntegerField()


class Client(models.Model):
	name = models.CharField(max_length=60, unique=True)
	address = models.ForeignKey(Address)
	phone = models.CharField(max_length=60, unique=True)
	email = models.EmailField(max_length=60, unique=True)

	def __str__(self):
		return self.name


class Cause(models.Model):
	name = models.CharField(max_length=60, unique=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS_CHOICES = (
		('E', 'ENTREGADA'),
		('EP', 'EN PROCESO'),
		('EF', 'EN FILA'),
		('PT', 'PROD. TERM.'),
	)
	client = models.ForeignKey(Client)
	user = models.ForeignKey(User)
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	statsus = models.CharField(max_length=12, choices=STATUS_CHOICES, default='E')


class ProcessOrder(models.Model):
	order = models.ForeignKey(Order)
	client = models.ForeignKey(Client)
	tire = models.ManyToManyField(Tire)
	observations = models.CharField(max_length=100)
	initial_inspection = models.CharField(max_length=100)
	scrape = models.CharField(max_length=100)
	cardeo = models.CharField(max_length=100)
	repair = models.CharField(max_length=100)
	encementado = models.CharField(max_length=100)
	filled = models.CharField(max_length=100)
	embandado = models.CharField(max_length=100)
	ft = models.FloatField()
	kg = models.FloatField()
	patch = models.CharField(max_length=100)

