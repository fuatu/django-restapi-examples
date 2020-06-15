from sixthapp.models import Author, Book
from sixthapp.serializer import AuthorSerializer, BookSerializer
from rest_framework import viewsets

# this example has nested serializers. Check serializer.py
# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer