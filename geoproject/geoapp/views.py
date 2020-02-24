from django.shortcuts import render
from .models import Aircraft, Operator, AircraftLoacation
from .serializers import AircraftSeralizer, OperatorSerializer, AircraftLocationSerializer,AircraftModelSeralizer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse



class OperatorView(APIView):
    def get_object(self, pk):
        try:
            return Operator.objects.get(pk=pk)
        except Operator.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        operator = self.get_object(pk)
        serializer = OperatorSerializer(operator)
        return JsonResponse(serializer.data)

class AircraftView(APIView):
    def get(self, request, pk, format=None):
        aircrafts = Aircraft.objects.all().filter(pk=pk).select_related('operator')
        if aircrafts:
            print(aircrafts[0].r_id)
            print(aircrafts[0].operator.id)
            import datetime
            serializer = AircraftModelSeralizer(aircrafts[0],context={'hoge':datetime.datetime.now()})
            return JsonResponse(serializer.data, safe=False) # TODO safe=False
        else:
            return JsonResponse()
            

class AircraftListView(APIView):
    def get(self, request, format=None):
        aircrafts = Aircraft.objects.all()
        serializer = AircraftSeralizer(aircrafts, many=True)
        return JsonResponse(serializer.data, safe=False) # TODO safe=False

    def post(self, request, format=None):
        serializer = AircraftSeralizer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.get('r_id'))
            print(serializer.validated_data.get('operator'))
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class AircraftLocationView(APIView):
    def get(self, request, format=None):
        locations = AircraftLoacation.objects.all()
        serializer = AircraftLocationSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = AircraftLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)