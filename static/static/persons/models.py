from django.db import models
from languages.models import Languages

# Create your models here.

class Persons(models.Model):
    first_name = models.TextField()
    sir_name = models.TextField()
    last_name = models.TextField()
    # languageID = models.ForeignKey(Languages)
