
from rest_framework.views import APIView

from fileupload.models import File
from fileupload.serializers import FileSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.

class FileUploadView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializer
    queryset = File.objects.all()

