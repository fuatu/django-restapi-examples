from fourthapp.models import Student
from fourthapp.serializers import StudentSerializer
from rest_framework import generics


# Using classes for views with generics
# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer