from rest_framework import serializers
from .models import Book  # Assuming the Book model exists in api/models.py

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields from the  book model

