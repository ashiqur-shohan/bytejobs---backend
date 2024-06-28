from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField
# Create your models here.

EDUCATION_CHOICES = [
    ('ssc', 'SSC'),
    ('hsc', 'HSC'),
    ('honours', 'HONOURS'),
    ('masters', 'MASTERS'),
]
USER_TYPE = [
    ('employee', 'EMPLOYEE'),
    ('employer', 'EMPLOYER')
]

LOCATIONS_OPTIONS = (
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
)


class CustomUserModel(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYEE = 'EMPLOYEE', 'Employee'
        EMPLOYER = 'EMPLOYER', 'Employer'
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    role = models.CharField(max_length=50, choices=Role.choices)
    phone_num = PhoneNumberField()
    slug = AutoSlugField(populate_from='username')

    class Meta:
        db_table = 'custom_user_table'


class EmployeeModel(models.Model):
    user = models.OneToOneField(
        CustomUserModel, on_delete=models.CASCADE, related_name='employee_model')
    birth_date = models.DateField(null=True)

    class Meta:
        db_table = 'employee_table'

    def __str__(self) -> str:
        return self.user.username


class EmployerModel(models.Model):
    user = models.OneToOneField(
        CustomUserModel, on_delete=models.CASCADE, related_name='employer_model')
    comp_name = models.CharField(max_length=50, unique=True)
    comp_location = models.CharField(max_length=100,choices=LOCATIONS_OPTIONS)
    comp_address = models.CharField(max_length=100)

    class Meta:
        db_table = 'employer_table'

    def __str__(self) -> str:
        return self.user.username
