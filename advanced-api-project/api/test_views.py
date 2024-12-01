from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data for all test cases."""
        self.client = APIClient()
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Sample Book", publication_year=2021, author=self.author
        )

    def test_create_book(self):
        """Test creating a new book."""
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id,
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_retrieve_book_list(self):
        """Test retrieving a list of books."""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {"title": "Updated Title"}
        response = self.client.patch(f'/api/books/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        """Test filtering books by title."""
        response = self.client.get('/api/books/?title=Sample Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching for books by a keyword."""
        response = self.client.get('/api/books/?search=Sample')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication_year."""
        Book.objects.create(title="Another Book", publication_year=2020, author=self.author)
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Another Book")
