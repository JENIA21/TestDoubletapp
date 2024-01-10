FROM python:3.11

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock*
COPY . .
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["alembic", "revision", "--autogenerate"]
CMD ["alembic", "upgrade", "head"]
CMD ["python", "main.py"]