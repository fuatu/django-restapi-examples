from fifthapp.models import Student
from fifthapp.serializers import StudentSerializer
from rest_framework import viewsets


# Using classes for views with viewsets with router
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer