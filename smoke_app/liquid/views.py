from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Liquid
from .serializers import LiquidSerializer

class LiquidViewSet(viewsets.ModelViewSet):
    queryset = Liquid.objects.all()
    serializer_class = LiquidSerializer