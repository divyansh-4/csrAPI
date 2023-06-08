from django.db import models

# Create your models here.
class Trip(models.Model):
    origin=models.CharField(max_length=64)
    destination=models.CharField(max_length=64)
    nights=models.IntegerField(max_length=64)
    price=models.IntegerField(max_length=64)

    def __str__(self):
        return f"{self.id}-{self.origin} To {self.destination} for {self.nights} nights costs {self.price} USD"