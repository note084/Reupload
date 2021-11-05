from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    seats = 24


    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration} minutes."

    def get_absolute_url(self):
        return reverse(
            'flights:detailpage',
            kwargs={
                "dest": self.destination,
                "orig": self.origin,
                "pk": self.pk

            }
        )


class FlightItems(models.Model):
    
    seats = 24
    quanitity = models.IntegerField()
    price = 199
    flight = models.ForeignKey(Flight, related_name='flight', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            'flights:add',
            kwargs={
                "pk": self.pk

            }
        )

class FlightObject(models.Model):
    items = models.ManyToManyField(FlightItems)