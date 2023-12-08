from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

