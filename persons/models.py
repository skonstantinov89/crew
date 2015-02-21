from django.db import models

# Create your models here.
class Positions(models.Model):
	name = models.TextField()
	exp = models.IntegerField()

class CV_Documents(models.Model):
	"""docstring for CV_Documents"""
	
	cv_file = models.FileField(upload_to='CVDocuments')
	date = models.DateField(auto_now=True)
			
class Languages(models.Model):
	name = models.TextField()
	score = models.IntegerField()
	# test commit
	
class Persons(models.Model):
    first_name = models.TextField()
    sir_name = models.TextField()
    last_name = models.TextField()
    languageID = models.ForeignKey(Languages)
    cvID = models.ForeignKey(CV_Documents)
    availableFrom = models.DateField()
    availableTo = models.DateField()
    positionID = models.ForeignKey(Positions)


class RecommendationFiles(models.Model):
	file = models.FileField(upload_to='RecommendFiles')
	date = models.DateField(auto_now=True)

class RecsMiddleware(models.Model):
	personID = models.ForeignKey(Persons)
	recID = models.ForeignKey(RecommendationFiles)

class OtherDocuments(models.Model):
	file = models.FileField(upload_to='OtherDocs')
	personID = models.ForeignKey(Persons)
