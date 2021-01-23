# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app/backend/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
 && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libressl-dev musl-dev libffi-dev

ADD ./app/backend/requirements/base.txt /usr/src/app/backend/requirements/base.txt
ADD ./app/backend/requirements/production.txt /usr/src/app/backend/requirements/production.txt

# install dependencies
RUN pip install --upgrade pip \
 && pip install -r ./requirements/production.txt

 # copy project
ADD ./app/backend/ /usr/src/app/backend/

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# add and run as non-root user
RUN adduser -D michal
RUN chown michal:michal -R /usr/src/app/backend/
USER michal


