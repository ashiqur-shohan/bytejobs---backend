from rest_framework import serializers
from .models import JobModel

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = '__all__'