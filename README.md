Working progress project.

# Event Sourcing prototype in Python

- Flask: micro-web framework
- Peewee: ORM
- Pymysql: DB driver
- Pytest

And event sourcing implement from scratch.

## Install

This project manages dependencies with `poetry`. Get `poetry` and run:

```
poetry install
```

Active virtual environment

```
poetry shell
```

## Run

Run server:

```
python main.py
```

Run unittest:

```
PYTHONPATH=. pytest
```