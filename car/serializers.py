from rest_framework import serializers
from .models import Car, Color, Manufacturer


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("title",)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("title",)


class CarReadSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Car
        depth = 1
        fields = "__all__"


class CarWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
