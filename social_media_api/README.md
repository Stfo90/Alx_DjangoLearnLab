Social Media API

This is a Social Media API built with Django and Django REST Framework (DRF). The API allows users to register, authenticate, create and manage posts, follow other users, and view a feed of posts from followed users.


---

Features

User Authentication: Register, login, and retrieve tokens for authentication.

User Profiles: View and edit user profiles, including bio and profile picture.

Posts: Create, update, delete, and view posts.

Comments: Add comments to posts and manage them.

Follows: Follow and unfollow users.

Feed: View posts from followed users, ordered by creation date.



---

Installation

1. Clone the repository:

git clone https://github.com/your_username/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api


2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Apply migrations and create a superuser:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


5. Start the development server:

python manage.py runserver




---

API Endpoints

Authentication


---

Posts


---

Comments


---

Follows


---

Feed


---

Usage Examples

1. Register a User

curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser",
    "password": "password123",
    "email": "test@example.com"
}'

2. Log In

curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser",
    "password": "password123"
}'

3. Follow a User

curl -X POST http://127.0.0.1:8000/api/accounts/follow/2/ \
-H "Authorization: Token <your_token>"

4. View Feed

curl -X GET http://127.0.0.1:8000/api/posts/feed/ \
-H "Authorization: Token <your_token>"


---

Development

To contribute:

1. Fork the repository.


2. Create a new branch:

git checkout -b feature-name


3. Make your changes and commit them:

git commit -m "Description of changes"


4. Push to your branch:

git push origin feature-name


5. Open a pull request.





---

Social Media API Documentation

Overview

This project is a Social Media API built with Django and Django REST Framework. It includes user authentication, posts, likes, follows, and notifications functionalities.


---

Endpoints

Accounts

1. Register a new user:

Endpoint: POST /accounts/register/

Request Body:

{
  "username": "testuser",
  "password": "testpassword",
  "email": "testuser@example.com"
}

Response:

{
  "token": "abcd1234efgh5678"
}



2. Login a user:

Endpoint: POST /accounts/login/

Request Body:

{
  "username": "testuser",
  "password": "testpassword"
}

Response:

{
  "token": "abcd1234efgh5678"
}



3. Follow a user:

Endpoint: POST /accounts/<user_id>/follow/

Response:

{
  "message": "You are now following user_id."
}



4. Unfollow a user:

Endpoint: POST /accounts/<user_id>/unfollow/

Response:

{
  "message": "You have unfollowed user_id."
}





---

Posts

1. Create a post:

Endpoint: POST /posts/

Request Body:

{
  "title": "My Post Title",
  "content": "This is the post content."
}

Response:

{
  "id": 1,
  "title": "My Post Title",
  "content": "This is the post content.",
  "author": "testuser",
  "created_at": "2024-12-13T12:00:00Z"
}



2. Like a post:

Endpoint: POST /posts/<post_id>/like/

Response:

{
  "message": "Post liked successfully."
}



3. Unlike a post:

Endpoint: POST /posts/<post_id>/unlike/

Response:

{
  "message": "Post unliked successfully."
}





---

Notifications

1. Get notifications:

Endpoint: GET /notifications/

Response:

[
  {
    "id": 1,
    "recipient": "testuser",
    "actor": "anotheruser",
    "verb": "liked your post",
    "timestamp": "2024-12-13T12:00:00Z"
  }
]



2. Mark a notification as read:

Endpoint: POST /notifications/<notification_id>/mark-read/

Response:

{
  "message": "Notification marked as read."
}





---

Usage Instructions

1. Clone the repository and navigate to the project directory:

git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api


2. Install dependencies:

pip install -r requirements.txt



