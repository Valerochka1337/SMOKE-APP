from .api import LiquidViewSet
from rest_framework import routers
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register('api/liquid', LiquidViewSet, 'liquid')
urlpatterns = router.urls