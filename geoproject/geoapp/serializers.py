from rest_framework import serializers
from .models import Aircraft, Operator, AircraftLoacation


class AircraftSeralizer(serializers.Serializer):
    r_id = serializers.CharField(required=True, max_length=50)
    operator = serializers.CharField(required=True, max_length=50)
    created_date = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", required=False, read_only=True)
    updated_date = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", required=False, read_only=True)


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ['id', 'name']


class AircraftLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftLoacation
        fields = ['aircraft','report','geom']