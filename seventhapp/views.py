from rest_framework import viewsets
from seventhapp.serializers import EmployeeSerializer
from seventhapp.models import Employee
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

# this example for basic authentication
# uses is authenticated and also django model permissions - class level
# for global level go to settings.py and set DEFAULT_AUTHENTICATION_CLASSES, DEFAULT_PERMISSION_CLASSES
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]