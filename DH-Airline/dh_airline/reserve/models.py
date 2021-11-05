from django.db import models
from django.utils import timezone


# Create your models here.
class Reserve(models.Model):
    businessClass = 30
    confirmation = models.CharField(max_length=8)