from rest_framework import serializers
from .models import EmployerModel,EmployeeModel,CustomUserModel


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone_num', 'password', 'slug']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserModelSerializer()
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeeModel
        fields = ['user', 'confirm_password', 'birth_date']

    def save(self, **kwargs):
        user_data = self.validated_data['user']
        confirm_password = self.validated_data['confirm_password']
        birth_date = self.validated_data['birth_date']

        # Extract user data
        username = user_data['username']
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        email = user_data['email']
        phone_num = user_data['phone_num']
        password = user_data['password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'error': 'Password does not match.'})

        user = CustomUserModel(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_num=phone_num,
            role=CustomUserModel.Role.EMPLOYEE
        )
        user.set_password(password)
        user.save()

        employee = EmployeeModel(user=user, birth_date=birth_date)
        employee.save()

        return employee
    
class EmployerSerializer(serializers.ModelSerializer):
    user = CustomUserModelSerializer()
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = EmployerModel
        fields = ['user', 'confirm_password',
                  'comp_name', 'comp_address', 'comp_location']
    def save(self, **kwargs):
        user_data = self.validated_data['user']
        confirm_password = self.validated_data['confirm_password']
        comp_name = self.validated_data['comp_name']
        comp_address = self.validated_data['comp_address']
        comp_location = self.validated_data['comp_location']
        # Extract user data
        username = user_data['username']
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        email = user_data['email']
        phone_num = user_data['phone_num']
        password = user_data['password']
        if password != confirm_password:
            raise serializers.ValidationError(
                {'error': 'Password does not match.'})
        user = CustomUserModel(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_num=phone_num,
            role=CustomUserModel.Role.EMPLOYER
        )
        user.set_password(password)
        user.save()

        employer = EmployerModel(
            user=user, comp_name=comp_name, comp_address=comp_address, comp_location=comp_location)
        employer.save()

        return employer
