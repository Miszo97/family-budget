# syntax=docker/dockerfile:1
FROM python:3
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 
ENV \
    POETRY_VERSION=1.1.11 \
    POETRY_HOME="/opt/poetry" 
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /code
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-root
COPY . /code/
