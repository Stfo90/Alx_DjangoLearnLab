from rest_framework import serializers
from .models import Author, Book

# BookSerializer serializes all fields of the Book model.
# It includes custom validation to ensure the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation
    def validate_publication_year(self, value):
        from datetime import datetime
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer includes a nested BookSerializer to dynamically serialize
# all books associated with an author.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for books

    class Meta:
        model = Author
        fields = ['name', 'books']

