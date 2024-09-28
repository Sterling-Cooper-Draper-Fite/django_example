# Run in Docker

Define custom environment variables in a docker-compose.override.yml file:

```yml
# docker-compose.override.yml
services:
  server:
    environment:
      AWS_STORAGE_BUCKET_NAME: my-bucket-name
      AWS_JOB_QUEUE_URL: https://sqs.us-east-1.amazonaws.com/123456789012/my-queue-name
```

Use `docker compose` to build and run the services:

```bash
# build the images
docker compose build

# run the services
aws-vault exec my-profile-name
docker compose up

# run management tasks
docker compose run server python manage.py migrate
```
