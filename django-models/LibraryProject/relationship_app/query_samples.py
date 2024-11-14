from .models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()  # Find the author by name
    books = Book.objects.filter(author=author)  # Filter books by author
    return books

# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()  # Find the library by name
    books = library.books.all() if library else []  # Get all books in the library
    return books

# Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()  # Find the library by name
    librarian = library.librarian if library else None  # Get the associated librarian
    return librarian
