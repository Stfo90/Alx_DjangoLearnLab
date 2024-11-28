# Advanced API Development with Django REST Framework

## Overview
This project demonstrates advanced API concepts using Django REST Framework (DRF). It includes custom serializers, views, permissions, and CRUD operations for managing books and authors.

## API Endpoints

### Books

- **GET `/books/`**  
  Lists all books in the database.  
  No authentication required.

- **GET `/books/<id>/`**  
  Retrieves details of a specific book by ID.  
  No authentication required.

- **POST `/books/create/`**  
  Creates a new book.  
  **Authentication required** (only authenticated users can create books).

- **PUT `/books/<id>/update/`**  
  Updates an existing book by ID.  
  **Authentication required** (only authenticated users can update books).

- **DELETE `/books/<id>/delete/`**  
  Deletes an existing book by ID.  
  **Authentication required** (only authenticated users can delete books).

### Permissions
- **IsAuthenticatedOrReadOnly** permission class is used to protect `POST`, `PUT`, and `DELETE` views.  
  Unauthenticated users can only access `GET` views for reading data.

## Running the Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
