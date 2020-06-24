from rest_framework import viewsets, generics
from seventhapp.serializers import EmployeeSerializer, NoModelSerializer
from seventhapp.models import Employee
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError

# this example for basic authentication
# uses is authenticated and also django model permissions - class level
# for global level go to settings.py and set DEFAULT_AUTHENTICATION_CLASSES, DEFAULT_PERMISSION_CLASSES
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    list:
    for list you can use also id and name for search

    **examples**

    - /seventhapp/employees/?id=1
    - /seventhapp/employees/?name=aaa
    - /seventhapp/employees/?id=1&name=aaa

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        queryset = self.queryset
        if not self.request.query_params:
            return queryset
        # for id
        try:
            id = self.request.query_params['id']
        except MultiValueDictKeyError:
            id = ""
        # for name
        try:
            name = self.request.query_params['name']
        except MultiValueDictKeyError:
            name = ""
        if id:
            queryset = queryset.filter(id=id)
        if name:
            queryset = queryset.filter(name=name)
        return queryset


@api_view(['GET', ])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated,])
def check_token(request):
    if request.method == 'GET':
        return_json = {"detail": "Success"}
        return Response(return_json, status=status.HTTP_200_OK)


class NoModelView(generics.GenericAPIView):
    serializer_class = NoModelSerializer
    def post(self, request):
        serializer = NoModelSerializer(data=request.data)
        if serializer.is_valid():
            # do something
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)