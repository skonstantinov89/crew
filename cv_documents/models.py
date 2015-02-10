from django.db import models

# Create your models here.

class CV_Documents(models.Model):
	"""docstring for CV_Documents"""
	
	file = models.FileField(upload_to='CVDocuments')
	date = models.DateField(auto_now=True)

		