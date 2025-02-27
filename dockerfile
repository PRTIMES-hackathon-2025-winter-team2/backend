FROM python:3.13.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "python", "main.py"]
