# Django Example

## Getting Started

```bash
# create and activate an anaconda environment (first time)
conda env create --file environment.yml
conda activate django-example

# update and activate your local anaconda environment
conda env update --file environment.yml --prune
conda activate django-example

# run database migrations
python manage.py migrate

# start the django server
python manage.py runserver

# run linter
flake8 .

# check formatting
black --check .

# check imports
isort --check .
```

## Tools

* black - auto formatter
* flake8 - linting
* mypy - type checking
* pytest - unit test framework
* poetry - dependency management
* isort - sorting imports
