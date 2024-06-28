from django.contrib import admin
from .models import JobModel
# Register your models here.


@admin.register(JobModel)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary_min',
                    'salary_max', 'work_time', 'work_type']
