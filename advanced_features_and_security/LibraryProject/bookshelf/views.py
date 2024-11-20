from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from your_app_name.models import Document

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
