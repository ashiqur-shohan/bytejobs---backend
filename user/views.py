from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import EmployeeSerializer, EmployerSerializer, UserLoginSerializer
from .models import EmployeeModel,EmployerModel
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
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


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'loginsuccesful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)