from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Venex (models.Model): 
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()