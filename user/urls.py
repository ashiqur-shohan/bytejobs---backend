from django.urls import path, include
from rest_framework import routers
from . import views
# router = routers.DefaultRouter()
# router.register('employee/registration', views.EmployeeView,
#                 basename='employee_registration')
urlpatterns = [
    path('employee/',views.EmployeeView.as_view(),name='employee_registration' ),
    path('employee/<slug:slug>', views.EmployeeDetailView.as_view(),name='employee_details'),
    # path('',include(router.urls))
]
