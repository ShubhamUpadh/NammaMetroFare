from django.db import models

class Station(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name

class Fare(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='origin_fares')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='destination_fares')
    fare_amount = models.DecimalField(max_digits=10, decimal_places=2)