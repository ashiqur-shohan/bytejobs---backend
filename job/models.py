from django.db import models
from user.models import EmployerModel
# Create your models here.

WORK_TYPE_OPTIONS = (
    ('Remote', 'Remote'),
    ('On-Site', 'On-Site'),
    ('Hybrid', 'Hybrid'),
)

WORK_TIME_OPTIONS = (
    ('Contractual', 'Contractual'),
    ('Part-Time', 'Part-Time'),
    ('Full-Time', 'Full-Time'),
    ('Intern', 'Intern'),
)


class JobModel(models.Model):
    employer = models.ForeignKey(
        EmployerModel, related_name='job_model', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    posted_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    dead_line = models.DateField(null=True)
    requirements = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    experience_min = models.IntegerField()
    experience_max = models.IntegerField()
    work_time = models.CharField(
        max_length=20, choices=WORK_TIME_OPTIONS, default='Full-Time')
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPE_OPTIONS, default='On-Site')

    def __str__(self) -> str:
        return self.title
