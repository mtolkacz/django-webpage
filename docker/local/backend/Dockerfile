# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app/backend/

# set environment variables+
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
 && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libressl-dev musl-dev libffi-dev

COPY ./app/backend/requirements/base.txt /usr/src/app/backend/requirements/base.txt
COPY ./app/backend/requirements/local.txt /usr/src/app/backend/requirements/local.txt

# install dependencies
RUN pip install --upgrade pip \
 && pip install -r ./requirements/local.txt

 # copy project
COPY ./app/backend/ /usr/src/app/backend/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/backend/entrypoint.local.sh"]
