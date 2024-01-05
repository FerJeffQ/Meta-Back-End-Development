from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name + " : " + self.cuisine