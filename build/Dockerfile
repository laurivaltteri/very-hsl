FROM python:3.9.8-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

ADD poetry.lock pyproject.toml ./
ADD .env ./

RUN pip install poetry psycopg2
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-dev 
ADD ./veri_hsl /app


ENV TIMEOUT=1200
ENV GRACEFUL_TIMEOUT=1200
ENV MAX_WORKERS=1
ENV APP_MODULE=veri_hsl.main:app
ENV APP=prod

#RUN bash -c "source $HOME/.poetry/env"
CMD ["python", "/app/main.py"]