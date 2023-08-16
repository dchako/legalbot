from rest_framework import serializers
from .models import Partner, Partnership, Manager
from rest_framework.exceptions import NotFound


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

    partnership = PartnershipSerializer(read_only=True)
    partnership_id = serializers.IntegerField()

    def create(self, validated_data):
        ''' Method to create a new Manager'''

        try:
            Partnership.objects.get(
                pk=int(validated_data.get('partnership_id'))
            )
        except Partnership.DoesNotExist:
            raise NotFound('Expansion not Encontrado!')

        return Manager.objects.create(**validated_data)

    class Meta:
        model = Manager
        fields = ['name', 'rut', 'pk', 'capacity', 'partnership_id']
        extra_kwargs = {
            'name': {'required': True},
            'rut': {'required': True},
            'capacity': {'required': True},
            'partnership_id': {'required': True}
        }


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    ''' Class to serialize the Partner model '''

    partnership = PartnershipSerializer(read_only=True)
    partnership_id = serializers.IntegerField()

    def create(self, validated_data):
        ''' Method to create a new Partner'''

        try:
            Partnership.objects.get(
                pk=int(validated_data.get('partnership_id'))
            )
        except Partnership.DoesNotExist:
            raise NotFound('Expansion not Encontrado!')

        return Partner.objects.create(**validated_data)

    class Meta:
        model = Partner
        fields = ['name', 'pk', 'entry', 'address', 'partnership_id']
        extra_kwargs = {
            'name': {'required': True},
            'entry': {'required': True},
            'address': {'required': True},
            'partnership_id': {'required': True}
        }
