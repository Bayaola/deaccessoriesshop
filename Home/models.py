from unicodedata import name
from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=250)
    grade = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = ImageField(blank=True, manual_crop="")
    
    def __str__(self):
        return self.name