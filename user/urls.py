from django.urls import path, include
from rest_framework import routers
from .views import EmployeeRegistrationView, EmployeeDetailView,EmployerRegistrationView,EmployerDetailView,UserLoginView
# router = routers.DefaultRouter()
# router.register('employee/registration', views.EmployeeView,
#                 basename='employee_registration')
urlpatterns = [
    path('/employee/', EmployeeRegistrationView.as_view(),
         name='employee_registration'),
    path('/employee/<slug:slug>',
         EmployeeDetailView.as_view(), name='employee_details'),
    path('/employer/', EmployerRegistrationView.as_view(),
         name='employer_registration'),
    path('/employer/<slug:slug>',
         EmployerDetailView.as_view(), name='employer_details'),
    path('/login/', UserLoginView.as_view(), name='login'),
    # path('',include(router.urls))
]
