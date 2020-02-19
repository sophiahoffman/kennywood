from django.db import models
from .customer import Customer
from .attraction import Attraction

class Itinerary(models.Model):

    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    starttime = models.IntegerField()

    class Meta:
        ordering = ("starttime",)
        verbose_name = ("itinerary")
        verbose_name_plural = ("itineraries")

    def __str__(self):
        return f'Riding {self.attraction.name} at {self.starttime}'
