# family-budget
API for the family budget application

# Installation 

### Clone repository
```
git clone https://github.com/Miszo97/family-budget.git
cd family-budget
```
### Set up env file
```
cp ./env_example ./env
````
### Build and run cointainers
```
docker-compose up
```

### You can load fixtures
```
docker-compose exec web poetry run python manage.py loaddata fixtures/*
```

## Play with the API

### Create a user
```
curl --location --request POST 'http://localhost:8000/api/users/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "admin"
}'
```

### Get a token
```
curl --location --request POST 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "admin"
}
```

### Create a new budget
```
curl --location --request POST 'http://localhost:8000/api/users/me/budgets/' \
--header 'Authorization: Bearer YOUR_ACCESS_KEY \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Budget",
    "income": 1000,
    "expenses": [{"amount": 100, "category": "HOME"}, {"amount": 100, "category": "TRAVEL"}, {"amount": 100, "category": "ENTERTAINMENT"}],
    "shared_accounts": [2,5]
}'
```

### Get your budgets
```
curl --location --request GET 'http://localhost:8000/api/users/me/budgets/ \
--header 'Authorization: Bearer YOUR_API_KEY'
```
with pagination
```
curl --location --request GET 'http://localhost:8000/api/users/me/budgets/?offset=0&limit=10' \
--header 'Authorization: Bearer YOUR_API_KEY'
```
you can also filter your result by name
```
curl --location --request GET 'http://localhost:8000/api/users/me/budgets/?name=Budget \
--header 'Authorization: Bearer YOUR_API_KEY'
```

### Get your shared budgets
```
curl --location --request GET 'http://localhost:8000/api/users/me/shared-budgets/?offset=0&limit=10' \
--header 'Authorization: Bearer YOUR_API_KEY'
```