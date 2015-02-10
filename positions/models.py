from django.db import models

# Create your models here.

class Positions(models.Model):
	name = models.TextField()
	exp = models.IntegerField()
	