from django.test import TestCase
from seventhapp.models import Employee

# models test
class TestEmployee(TestCase):

    def test_create(self, id="10000", name="a testing name", salary=10.11):
        self.assertTrue(Employee.objects.create(id=id, name=name, salary=salary))
        employee = Employee.objects.get(id=id)
        self.assertTrue(employee.__str__() == "10000a testing name10.11")
        self.assertTrue(employee.delete())


