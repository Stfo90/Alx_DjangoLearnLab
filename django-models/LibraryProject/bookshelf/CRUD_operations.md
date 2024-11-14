### Create a Book Instance
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

<Book: 1984 by George Orwell>

--------------------------------------------

### Retrieve the Book
```python
book = Book.objects.get(title="1984")
book

<Book: 1984 by George Orwell>

--------------------------------------------

### Update the Book Title
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

<Book: Nineteen Eighty-Four by George Orwell>

-------------------------------------------

### Delete the Book
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

<QuerySet []>
