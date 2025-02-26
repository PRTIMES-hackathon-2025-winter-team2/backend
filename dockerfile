FROM python:3.13.2

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "flask", "--app", "./server/main.py", "run", "--host=0.0.0.0"]
