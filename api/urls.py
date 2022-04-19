from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from api import views
app_name = 'api'

router = DefaultRouter()
router.register('unitMeasure', viewset=views.unitMeasureMVS, basename='unitmeasure')



urlpatterns = [
    path('', include(router.urls))
]