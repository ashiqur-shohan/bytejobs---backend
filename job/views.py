from django.shortcuts import render
from .serializers import JobSerializer
from .models import JobModel
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import BasePermission, SAFE_METHODS
# Create your views here.


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class JobView(viewsets.ModelViewSet):
    queryset = JobModel.objects.all().order_by('-posted_date')
    serializer_class = JobSerializer
    # specifying which filter to be applied
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'comp_name', 'work_mode', 'work_type']
    permission_classes = [IsOwnerOrReadOnly]
