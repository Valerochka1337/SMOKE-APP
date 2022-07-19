from .models import Liquid
from rest_framework import viewsets, permissions
from .serializers import LiquidSerializer

class LiquidViewSet(viewsets.ModelViewSet):
    queryset = Liquid.objects.all()
    permission_classes = [
        permissions.AllowAny
        ]
    serializer_class = LiquidSerializer