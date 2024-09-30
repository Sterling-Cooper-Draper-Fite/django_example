# Local Development

```bash
# create and activate an anaconda environment (first time)
conda env create --file environment.yml
conda activate django-example

# update and activate your local anaconda environment
conda env update --file environment.yml --prune
conda activate django-example

# set required environment variables
conda env config vars set EXAMPLE_MEDIA_BUCKET_NAME=my-bucket-name
conda env config vars set EXAMPLE_JOB_QUEUE_NAME=my-queue-name
conda env config vars set EXAMPLE_SERVER_TASK_ROLE_NAME=my-server-task-role-name
conda env config vars set EXAMPLE_WORKER_TASK_ROLE_NAME=my-worker-task-role-name
conda env config vars set DATABASE_URL=postgres://postgres:postgres@db:5432/django_example
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
