from rest_framework import serializers
from seventhapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary']


class NoModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, allow_blank=True)
    token = serializers.CharField(max_length=20)
    score = serializers.DecimalField(max_digits=4,decimal_places=2)