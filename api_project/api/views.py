from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import BasePermission

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for handling CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#Allows access only to authenticated usees.

class SecureDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user}!"})
# Restricts access to admin users.
class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Welcome, Admin!"})


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user




