from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from api import views
app_name = 'api'

router = DefaultRouter()
router.register('unitMeasure', viewset=views.UnitMeasureMVS, basename='unitmeasure')
router.register('status', viewset=views.StatusMVS, basename='status')
router.register('people', viewset=views.PeopleMVS, basename='people')
router.register('attachment', viewset=views.AttachmentMVS, basename='attachment')


urlpatterns = [
    path('', include(router.urls))
]