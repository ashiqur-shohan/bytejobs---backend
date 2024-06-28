from rest_framework import serializers
from . import models


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUserModel
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone_num', 'password', 'slug']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserModelSerializer()
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = models.EmployeeModel
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

        user = models.CustomUserModel(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_num=phone_num,
            role=models.CustomUserModel.Role.EMPLOYEE
        )
        user.set_password(password)
        user.save()

        employee = models.EmployeeModel(user=user, birth_date=birth_date)
        employee.save()

        return employee
