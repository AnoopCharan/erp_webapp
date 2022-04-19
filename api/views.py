from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api import models, serializers

# Create your views here.

class unitMeasureMVS(ModelViewSet):
    queryset = models.unitMeasure.objects.all()
    serializer_class = serializers.unitMeasureSerializer
    filter_fields = {
        'unit':['icontains', 'iregex']
    }
