from rest_framework import serializers
from clients.models import Client,Country


class ClientSerializer(serializers.ModelSerializer):
    '''
    this  serializer for serialize the data of client model
    in all fields
    '''
    class Meta:
        model=Client        #model
        fields='__all__'    #All fields of client model


    def create(self, validated_data):
        obj = Client.objects.using("clients").create(**validated_data)
        obj.save()
        return obj


class CountrySerializer(serializers.ModelSerializer):
    '''
    this serializer for serialize the data of country model
    in all fields
    '''
    class Meta:
        model=Country        #model
        fields='__all__'    #All fields of country model

    def create(self, validated_data):
        obj = Country.objects.using("clients").create(**validated_data)
        obj.save()
        return obj

class ClientViewSerializer(serializers.ModelSerializer):
    '''
    this serializer for serialize the data of country model 
    and country model to appear country data not id 
    in all fields
    '''
    country=CountrySerializer()
    class Meta:
        model=Client        #model
        fields='__all__'    #All fields of client model

    def create(self, validated_data):
        obj = Client.objects.using("clients").create(**validated_data)
        obj.save()
        return obj