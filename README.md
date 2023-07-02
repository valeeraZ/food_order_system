# food_order_system

A food order system for customers and restaurants. Customers can order food to take away or to be delivered to their home. Restaurants can receive orders and prepare them for customers.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m food_order_system
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "food_order_system"
food_order_system
├── domain # Domain layer with business logic
│   ├── user
├── infra
│   ├── db
│   │   ├── migrations # Contains all alembic migrations.
│   │   ├── model  # Contains all sqlalchemy models.
│   │   ├── repository # Contains repositories for all models using sqlalchemy.
│   │   ├── __init__.py # function load all models
│   │   ├── dependencies.py # Contains functions for database session.
│   │   ├── meta.py
│   │   └── utils.py
│   ├── rabbit
│   │   ├── dependencies.py
│   │   └── lifetime.py
├── tests
├── usecase # # Contains all use cases with Command Query Responsibility Segregation.
│   ├── user
│   └── __init__.py
├── web
│   ├── api
│   │   ├── routes # Contains all FastAPI routes.
│   │   └── __init__.py
│   ├── __init__.py
│   ├── application.py # Contains FastAPI application start point.
│   └── lifetime.py # Contains all dependencies for launching and stopping FastAPI application.
├── __init__.py
├── __main__.py # Contains entry point for running the application.
└── settings.py # Contains all settings for the application.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "FOOD_ORDER_SYSTEM_" prefix.

For example if you see in your "food_order_system/settings.py" a variable named like
`random_parameter`, you should provide the "FOOD_ORDER_SYSTEM_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `food_order_system.settings.Settings.Config`.

An example of .env file:
```bash
FOOD_ORDER_SYSTEM_RELOAD="True"
FOOD_ORDER_SYSTEM_PORT="8000"
FOOD_ORDER_SYSTEM_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);


You can read more about pre-commit here: https://pre-commit.com/


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=food_order_system" -e "POSTGRES_USER=food_order_system" -e "POSTGRES_DB=food_order_system" postgres:13.8-bullseye
```


2. Run the pytest.
```bash
pytest -vv .
```
