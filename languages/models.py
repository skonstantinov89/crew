from django.db import models

# Create your models here.

class Languages(models.Model):
	name = models.TextField()
	score = models.IntegerField()