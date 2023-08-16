from rest_framework import serializers
from .models import Partner, Partnership, Manager


class PartnershipSerializer(serializers.HyperlinkedModelSerializer):
    ''' Class to serializar the Partnership model '''

    def create(self, validated_data):
        return Partnership.objects.create(**validated_data)

    class Meta:
        model = Partnership
        fields = ['name', 'pk', 'rut']
        extra_kwargs = {
            'name': {'required': True},
            'rut': {'required': True}
        }


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    ''' Class to serialize the Manager model '''

    class Meta:
        model = Manager
        fields = ['name', 'rut', 'pk', 'capacity']
        extra_kwargs = {
            'name': {'required': True},
            'rut': {'required': True},
            'capacity': {'required': True}
        }


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    ''' Class to serialize the Partner model '''

    class Meta:
        model = Partner
        fields = ['name', 'pk', 'entry', 'address', 'rut']
