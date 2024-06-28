from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import EmployeeSerializer,EmployerSerializer
from .models import EmployeeModel,EmployerModel
# Create your views here.

# class EmployeeView(ModelViewSet):
#     serializer_class = serializers.EmployeeSerializer
#     queryset = models.EmployeeModel.objects.all()


class EmployeeRegistrationView(APIView):
    serializer_class = EmployeeSerializer

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EmployeeDetailView(APIView):
    def get(self, request, slug):
        data = EmployerModel.objects.all()
        serializer = EmployerSerializer(data, many=True)
        if slug:
            data = get_object_or_404(EmployeeModel, user__slug=slug)
            serializer = EmployeeSerializer(data)
        return Response(serializer.data)
        # return Response(serializer.errors)


class EmployerRegistrationView(APIView):
    serializer_class = EmployerSerializer

    def post(self, request):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class EmployerDetailView(APIView):
    def get(self, request, slug):
        data = EmployerModel.objects.all()
        serializer = EmployerSerializer(data, many=True)
        if slug:
            data = get_object_or_404(EmployerModel, user__slug=slug)
            serializer = EmployerSerializer(data)
        return Response(serializer.data)
        # return Response(serializer.errors)
