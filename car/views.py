from rest_framework import viewsets
from .models import Car
from .serializers import CarReadSerializer, CarWriteSerializer


class CarView(viewsets.ModelViewSet):
    serializer_class = CarReadSerializer
    queryset = Car.objects.all()

    action_serializers = {
        'create': CarWriteSerializer,
        'update': CarWriteSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super(CarView, self).get_serializer_class()
