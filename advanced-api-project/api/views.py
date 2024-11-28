from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(ListAPIView):
"""
    View for listing all books.
    This view does not require authentication and returns a list of books in the database.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveAPIView):
   """
    View for retrieving a single book by its ID.
    This view does not require authentication and returns the details of a specific book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(CreateAPIView):
"""
    View for creating a new book.
    This view is protected by authentication, meaning only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(UpdateAPIView):
"""
    View for updating an existing book.
    This view is protected by authentication, meaning only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(DestroyAPIView):
"""
    View for deleting a book.
    This view is protected by authentication, meaning only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



