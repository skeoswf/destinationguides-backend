from django.db import models
from .region import Region

class Country(models.Model):
  
  name = models.CharField(max_length=50)
  region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='countries')
