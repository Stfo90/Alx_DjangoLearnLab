# Django Admin Configuration for Book Model

## Registering the Book Model
- Imported the `Book` model in `bookshelf/admin.py`.
- Registered the model with the Django admin site to make it accessible.

## Customizing the Admin Interface
- **List Display**: Configured `list_display` to show `title`, `author`, and `publication_year` for each `Book` entry.
- **Search Fields**: Configured `search_fields` to enable searching by `title` and `author`.
- **List Filter**: Added a filter on `publication_year` to filter books by the year they were published.
