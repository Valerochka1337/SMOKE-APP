from .api import NewsViewSet
from rest_framework import routers
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register('api/news', NewsViewSet, 'news')
urlpatterns = router.urls