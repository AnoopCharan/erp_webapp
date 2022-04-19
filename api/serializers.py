from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from api import models

class unitMeasureSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='api:unitmeasure-detail')
    class Meta:
        model = models.unitMeasure
        fields = '__all__'