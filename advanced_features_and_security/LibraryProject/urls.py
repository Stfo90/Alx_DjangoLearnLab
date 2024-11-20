
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 
   path('admin/', admin.site.urls),
   path('relationship_app/', include('relationship_app.urls')),  # Include URLs from relationship_app
    # ... other project-level URLs
   path('bookshelf/', include('bookshelf.urls',
]




