## Groups and Permissions Setup

### Custom Permissions
- Added to the `Document` model:
  - can_view
  - can_create
  - can_edit
  - can_delete

### Groups
- **Viewers**: Assigned `can_view`.
- **Editors**: Assigned `can_create`, `can_edit`.
- **Admins**: Assigned all permissions.

### Testing
- Test users:
  - viewer_user: Can only view documents.
  - editor_user: Can view, create, and edit documents.
  - admin_user: Can perform all actions.
