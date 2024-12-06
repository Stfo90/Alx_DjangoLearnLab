# User Authentication System for Django Blog

## Overview
This user authentication system enables the following functionalities for the `django_blog` project:
- User Registration
- Login
- Logout
- Profile Management

### Features
1. **User Registration**  
   Users can create accounts using a username, password, and email.

2. **User Login and Logout**  
   Registered users can log in and out of their accounts securely.

3. **Profile Management**  
   Authenticated users can view and update their profile details.

---

## Setup Instructions

### 1. Installation
Ensure all dependencies are installed:
```bash
pip install django



# Blog Post Management Features

## Overview
This feature enables users to manage blog posts with full CRUD (Create, Read, Update, Delete) functionality.

## Features
1. **List all posts**: Accessible to all users at `/`.
2. **View post details**: Accessible to all users at `/posts/<id>/`.
3. **Create a new post**: Authenticated users can create posts at `/posts/new/`.
4. **Edit a post**: Only the author can edit posts at `/posts/<id>/edit/`.
5. **Delete a post**: Only the author can delete posts at `/posts/<id>/delete/`.

## Permissions
- Only authenticated users can create, edit, or delete posts.
- List and detail views are accessible to all users.

## Templates
- `post_list.html`: Displays all posts.
- `post_detail.html`: Shows a single post.
- `post_form.html`: Used for both creating and editing posts.
- `post_confirm_delete.html`: Confirms deletion.

## URLs
- `/`: List of all posts.
- `/posts/<id>/`: View post details.
- `/posts/new/`: Create a new post.
- `/posts/<id>/edit/`: Edit a post.
- `/posts/<id>/delete/`: Delete a post.



## Comment Functionality

### Features
- Authenticated users can add comments to blog posts.
- Authors of comments can edit or delete their comments.

### URLs
- Add Comment: `/post/<post_id>/comment/`
- Edit Comment: `/comment/<comment_id>/edit/`
- Delete Comment: `/comment/<comment_id>/delete/`

### Permissions
- Only authenticated users can add comments.
- Only the author of a comment can edit or delete it.

### Testing
- Verify adding, editing, and deleting comments.
- Ensure unauthorized actions are blocked.
