from django.urls import include, path

urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),  # Include URLs from relationship_app
    # ... other project-level URLs
]
