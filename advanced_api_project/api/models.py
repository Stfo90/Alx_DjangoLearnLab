
from django.db import models

# Author Model represents a book author with a name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores information about books, including their title, publication year,
# and the author who wrote them.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
# The one-to-many relationship is established with the Book model using a ForeignKey.

    def __str__(self):
        return self.title





