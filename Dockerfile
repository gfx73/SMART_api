FROM python:3.12

ENV PATH="/root/.local/bin:${PATH}"
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app
COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config installer.max-workers 10 && poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root --no-ansi

COPY ./app ./app

CMD ["python", "app/main.py"]