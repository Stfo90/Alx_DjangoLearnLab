from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
