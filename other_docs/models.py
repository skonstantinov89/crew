from django.db import models
from persons.models import Persons


# Create your models here.

class RecommendationFiles(models.Model):
	file = models.FileField(upload_to='RecommendFiles')
	date = models.DateField(auto_now=True)

class RecsMiddleware(models.Model):
	personID = models.ForeignKey(Persons)
	recID = models.ForeignKey(RecommendationFiles)

class OtherDocuments(models.Model):
	file = models.FileField(upload_to='OtherDocs')
	personID = models.ForeignKey(Persons)
