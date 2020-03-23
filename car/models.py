from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class DateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Color(DateTimeModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Manufacturer(DateTimeModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Car(DateTimeModel):
    MIN_YEAR = 1900
    MAX_YEAR = datetime.now().year

    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='car_color')
    year = models.PositiveIntegerField(validators=[
        MinValueValidator(MIN_YEAR),
        MaxValueValidator(MAX_YEAR)
    ])
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='car_manufacturer')

    def __str__(self):
        return f"car_id: {self.id}"
