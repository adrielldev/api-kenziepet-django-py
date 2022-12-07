from django.db import models
from numpy import log

class Animal(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NOT_INFORMED = 'NOT INFORMED'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOT_INFORMED, 'Not Informed'),
    ]

    name = models.CharField(max_length =50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length = 15,default='Not Informed',choices=SEX_CHOICES)
    group=models.ForeignKey(
        "groups.Group",on_delete = models.CASCADE,related_name = 'groups'
    )
    traits = models.ManyToManyField(
        "traits.Trait",related_name = 'traits'
    )
    def convert_dog_age_to_human_years(self):
        
        return 16 * log(int(self.age)) + 31

