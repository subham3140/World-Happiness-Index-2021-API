from django.db import models

# Create your models here.

class HappyIndexTable(models.Model):
    countryName = models.CharField(max_length=500, null=False)
    ladderScore = models.FloatField()
    healthyLifeExpectancy = models.FloatField()
    generosity = models.FloatField()
    gdp = models.FloatField()

    def __str__(self):
        return self.countryName
