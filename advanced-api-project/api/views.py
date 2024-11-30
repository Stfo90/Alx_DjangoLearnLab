# Allows filtering by fields such as title, author, and publication_year
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework import generics
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    # Fields for searching
    search_fields = ['title', 'author']  #author based on the author model
    # Fields for ordering results
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

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



