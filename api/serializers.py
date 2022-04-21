from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from api import models

class UnitMeasureSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='api:unitmeasure-detail')
    class Meta:
        model = models.UnitMeasure
        fields = '__all__'


class StatusSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='api:status-detail')
    class Meta:
        model = models.Status
        fields = '__all__'

class PeopleSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='api:people-detail')
    class Meta:
        model = models.People
        fields = '__all__'

class AttachmentSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='api:attachment-detail')
    class Meta:
        model = models.Attachment
        fields = '__all__'