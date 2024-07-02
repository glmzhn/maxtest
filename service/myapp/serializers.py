from rest_framework import serializers
from .models import Query, ExternalServerResponse


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'


class ExternalServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalServerResponse
        fields = '__all__'
