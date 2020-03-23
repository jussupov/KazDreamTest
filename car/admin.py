from django.contrib import admin
from .models import Car, Color, Manufacturer

[
    admin.site.register(model) for model in [Car, Color, Manufacturer]
]
