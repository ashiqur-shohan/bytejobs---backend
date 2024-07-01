from rest_framework import serializers
from .models import JobModel
from user.serializers import *

class EmployerJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerModel
        fields = ['comp_name', 'comp_address', 'comp_location']

    

class JobSerializer(serializers.ModelSerializer):
    # employer = EmployerJobSerializer()
    # comp_details = EmployerJobSerializer()
    comp_details = serializers.SerializerMethodField()
    class Meta:
        model = JobModel
        fields = '__all__'

    def get_comp_details(self, obj):
        employer = obj.employer
        return {
            'comp_name': employer.comp_name,
            'comp_address': employer.comp_address,
            'comp_location': employer.comp_location
        }
