from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarView

router = DefaultRouter()

router.register("cars", CarView, basename="cars")

urlpatterns = [
    path("", include(router.urls))
]
