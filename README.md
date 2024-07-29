# User Auth Service



## Description
Sample Flask app which supports basic user registration, login and get data operations

## Instructions for local setup

### Prerequisites:
1. SQLite DB - https://sqlitebrowser.org/dl/

### Steps to execute 
1. Clone the repo and checkout to ```main``` branch
2. Install requirements : ```pip install -r requirements.txt```
3. Run the app : ```python app.py```

### Sample requests
1. Health check
```curl
curl --location 'http://localhost:5000/health-check'
```
2. Register user
```curl
curl --location 'http://localhost:5000/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name" :"jainy",
    "middle_name" : null,
    "last_name" : null,
    "email" :"jainy.joy123@gmail.com",
    "password": "password@123"
}'
```
3. User Login
```curl
curl --location 'http://localhost:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email" :"jainy.joy123@gmail.com",
    "password": "password@123"
}'
```
4. Get user profile
```curl
curl --location 'http://localhost:5000/my-profile' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjIyMzYxOCwianRpIjoiM2ZjNDYyM2MtNTg1Mi00YTYzLTgwYTAtZjE0ZWQ0NmQ1YTI4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImphaW55LmpveTEyM0BnbWFpbC5jb20iLCJuYmYiOjE3MjIyMjM2MTgsImNzcmYiOiIxNjMyNWFhMi1hYWU1LTRiYTQtOWEyMS01MzJmMDhlZjAxZjEiLCJleHAiOjE3MjIyMjcyMTh9.5ZqaW3d3CZ7WJBpggsuxaHYRlxpBYIZz8o59w1lZHvA'

```