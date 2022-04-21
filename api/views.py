from traceback import print_tb
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api import models, serializers
from rest_framework.response import Response

# Create your views here.

class UnitMeasureMVS(ModelViewSet):
    queryset = models.UnitMeasure.objects.all()
    serializer_class = serializers.UnitMeasureSerializer
    filter_fields = {
        'unit':['icontains', 'iregex', 'exact']
    }

class StatusMVS(ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    filter_fields = {
        'status':['icontains', 'iregex', 'exact']
    }

class PeopleMVS(ModelViewSet):
    queryset = models.People.objects.all()
    serializer_class = serializers.PeopleSerializer
    filter_fields = {
        'firstName':['icontains', 'iregex', 'exact'],
        'lastName':['icontains', 'iregex', 'exact'],
        'email':['icontains', 'iregex', 'exact'],
    }

class AttachmentMVS(ModelViewSet):
    queryset = models.Attachment.objects.all()
    serializer_class = serializers.AttachmentSerializer
    filter_fields = {
        'fileName':['icontains', 'iregex', 'exact'],
        'contentType':['icontains', 'iregex', 'exact'],
    }

    def create(self, request, *args, **kwargs):
        # print(request.data)
        print(">>>>>>>>>>>",request.data['attachedFile'].content_type)
        print(">>>>>>>>>>>",request.data['attachedFile'].name)

        print(">>>>>>>>>>>",dir(request.data['attachedFile']))
        return 