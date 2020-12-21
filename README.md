# Webpage project
Creating blog entries, adding webpages and commenting

## Technologies
* Python 3.8<br>
* Django 3.1.4<br>
* Django Rest Framework 3.12.2<br>
* PostgreSQL 13.1<br>

## Requirements
TBA

## Functionalities
TBA

## Example env file
* Create .env file in docker-compose root directory /env/dev/.env or /env/prod/.env 
> SECRET_KEY={your_secret_key}
<br>DEBUG=1
<br>DATABASE=postgres
<br>SQL_ENGINE=django.db.backends.postgresql
<br>SQL_DATABASE=webpage
<br>SQL_USER={your_username}
<br>SQL_PASSWORD={your_password}
<br>SQL_HOST=db
<br>SQL_PORT=5432
<br>POSTGRES_USER={your_username}
<br>POSTGRES_PASSWORD={your_password}
<br>POSTGRES_DB=webpage
<br>SENTRY_SDK={your_sentry_url}
<br>GOOGLE_CLIENT_ID={your_client_id}
<br>GOOGLE_CLIENT_SECRET={your_client_secret}
## Run application from docker containers
> docker-compose -f local.yml up -d --build
## Live demo
TBA
