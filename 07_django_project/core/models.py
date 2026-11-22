from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name} - {self.price}$"
