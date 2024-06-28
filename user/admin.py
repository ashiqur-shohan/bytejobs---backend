from django.contrib import admin
from .models import EmployeeModel, EmployerModel, CustomUserModel
# Register your models here.


@admin.register(EmployerModel)
class EmployerAdmin(admin.ModelAdmin):
    # list_display = ['user', 'comp_name', 'comp_location']
    pass


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    # list_display = ['user', 'phone_num', 'education']
    pass


@admin.register(CustomUserModel)
class CustomUserModelAdmin(admin.ModelAdmin):
    # list_display = ['user', 'phone_num', 'education']
    pass
