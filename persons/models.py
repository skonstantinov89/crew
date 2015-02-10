from django.db import models
from languages.models import Languages
from cv_documents.models import CV_Documents
from positions.models import Positions
from languages.models import Languages

# Create your models here.

class Persons(models.Model):
    first_name = models.TextField()
    sir_name = models.TextField()
    last_name = models.TextField()
    languageID = models.ForeignKey(Languages)
    cvID = models.ForeignKey(CV_Documents)
    availableFrom = models.DateField()
    availableTo = models.DateField()
    positionID = models.ForeignKey(Positions)