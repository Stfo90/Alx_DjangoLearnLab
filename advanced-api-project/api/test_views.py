from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create an author and a book for testing
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

    def test_create_book_authenticated(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')

        # Data for a new book
        data = {
            "title": "New Test Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        # Send a POST request to create a book
        response = self.client.post('/api/books/', data)

        # Check response status and data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Test Book')

    def test_create_book_unauthenticated(self):
        # Attempt to create a book without logging in
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
