# Design Pattern for FastAPI Template

## Introduction
To maintain a consistent design pattern, we have created this repository to provide a template for new projects.

## Project Structure
The project structure is as follows:
```
design-pattern/
│
├── src/
│   ├── main.py
│   ├── __init__.py
│   ├── app/
│   │   ├── modules/
│   │   │   ├── passports/
│   │   │   ├── users/
│   │   │   │   ├── schemas/
│   │   │   │   ├── validators/
│   │   │   ├── users_controller.py
│   │   │   ├── users_service.py
│   │   │   ├── users_repo.py
│   │   │   ├── users_middleware.py
│   ├── config/
│   │   ├── config_service.py
│   ├── core/
│   │   ├── helpers/
│   │   ├── middlewares/
│   ├── db/
│   │   ├── db.py
│   ├── routers/
│   │   ├── v1/
│   │          └── users_route.py
│   │          └── passports_route.js
│   ├── utils/
│   │   ├── decorator/
│   │   ├── lib/
│
├── tests/
│   ├── users_e2e_test.py
│
├── venv
    ├── bin
    ├── include
    ├── lib
├── .env
├── .env.example
├── .flake8
├── poetry.lock
├── .gitignore
├── pyproject.toml
├── README.md


```

#### venv
Need to install virtual environment (venv)

`python -m venv venv` and `source venv/bin/activate` - These commands for mac

#### .flake8

`poetry run flake8`

flake8 primarily serves as a linter

#### code formatter for ./src

`poetry run format`

autopep8 primarily serves as a formatter

#### pylint

`poetry run pylint [file name]`

It establishes a solid foundation for maintaining code quality, consistency, and readability

#### pyproject.toml
It simplifies Python project management by centralizing configuration for dependencies and dev dependencies.

#### README.md
This file contains the documentation for the application. It is used to provide information about the application.

#### Requirements for this project

- Python
- Pip
- poetry

#### Run command for project

`poetry run uvicorn src.main:app --reload`

or 

`poetry run uvicorn src.main:app --reload --port ${PORT:-8080}` - Development with Auto-reload on a Specific Port

or

`poetry run python -m src.main` - Production Mode without Auto-reload

#### Run the command for installing any new package

`poetry add [package name]`

#### Run the command for installing dev dependencies

`poetry add --dev [package name]`

#### Run command after cloning

`poetry install`

#### Run command for test

`poetry run pytest`

#### Run command for single test

`poetry run pytest -k test_name`

#### code formatter for ./test

`poetry run format_test`
