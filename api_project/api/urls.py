from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList  # Import the ViewSet and the ListAPIView (from the previous task)

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Retain the previous ListAPIView
    path('', include(router.urls)),  # Include all routes registered with the router
]
