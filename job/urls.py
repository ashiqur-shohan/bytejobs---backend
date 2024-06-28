from django.urls import path, include
from .views import JobView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('', JobView, basename='job')
urlpatterns = [
    path('', include(router.urls))
]
