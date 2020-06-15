from fifthapp.models import Student
from fifthapp.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

# Using classes for views with viewsets with router
# no need to separate pk and list operations
# pagination class was added to show how to do class level pagination
# for global pagination check settings.py
# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 3

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination