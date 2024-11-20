from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from your_app_name.models import Document
from .models import Book

@permission_required('your_app_name.can_view', raise_exception=True)
def view_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return render(request, 'document_detail.html', {'document': document})

@permission_required('your_app_name.can_create', raise_exception=True)
def create_document(request):
    # Logic to create a document
    pass

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_document(request, document_id):
    # Logic to edit a document
    pass

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_document(request, document_id):
    # Logic to delete a document
    pass
# View to list all books
def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'book_list.html', {'books': books})

# View to show details of a specific book
def books(request, book_id):
    book = Book.objects.get(id=book_id)  # Retrieve a specific book by ID
    return render(request, 'book_detail.html', {'book': book})



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the book to the database
            return redirect('book_list')  # Replace 'book_list' with the name of your list view
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})
