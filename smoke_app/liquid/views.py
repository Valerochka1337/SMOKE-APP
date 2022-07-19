from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Liquid
from .serializers import LiquidSerializer
from .permissions import IsAdminOrReadOnly

class LiquidViewSet(viewsets.ModelViewSet):
    queryset = Liquid.objects.all()
    serializer_class = LiquidSerializer
    permission_classes = (IsAdminOrReadOnly,)