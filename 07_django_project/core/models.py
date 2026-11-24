from django.db import models
from django.conf import settings
class Asset(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.name} - {self.price}$"
