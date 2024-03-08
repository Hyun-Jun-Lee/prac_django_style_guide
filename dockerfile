FROM python:3.12.2

# Fix python printing
ENV PYTHONUNBUFFERED 1

# Installing all python dependencies
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/