from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from . import serializers
from . import models
# Create your views here.

# class EmployeeView(ModelViewSet):
#     serializer_class = serializers.EmployeeSerializer
#     queryset = models.EmployeeModel.objects.all()


class EmployeeView(APIView):
    serializer_class = serializers.EmployeeSerializer

    def post(self, request):
        serializer = serializers.EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EmployeeDetailView(APIView):
    def get(self, request, slug):
        data = models.EmployeeModel.objects.all()
        serializer = serializers.EmployeeSerializer(data, many=True)
        if slug:
            data = get_object_or_404(models.EmployeeModel, user__slug=slug)
            serializer = serializers.EmployeeSerializer(data)
        return Response(serializer.data)
        # return Response(serializer.errors)
