from pyexpat import model
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 20)
    scientific_name = models.CharField(max_length = 50)
    
