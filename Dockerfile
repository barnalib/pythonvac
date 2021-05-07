FROM python:3.7

# Creating Application Source Code Directory
RUN mkdir -p /usr/src/app

# Setting Home Directory for containers
WORKDIR /usr/src/app


RUN pip install requests

# Copying src code to Container
COPY . /usr/src/app

# Application Environment variables
#ENV APP_ENV development
ENV PORT 8080

# Exposing Ports
EXPOSE $PORT


# Running Python Application
CMD python /usr/src/app/testv.py
