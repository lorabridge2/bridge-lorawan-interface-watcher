FROM python:3.9-alpine as build

WORKDIR /home/controller
# RUN apk add --no-cache gcc libc-dev g++
# RUN pip install pipenv
RUN pip install --no-cache-dir pipenv
COPY Pipfile* ./
RUN pipenv install --system --clear
COPY . .

ENTRYPOINT [ "python3", "watcher.py" ]

