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





