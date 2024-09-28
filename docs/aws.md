# Using AWS

## Authentication

Use [aws-vault](https://github.com/99designs/aws-vault)

```bash
aws-vault exec my-profile-name
docker compose up
```

## Prerequisites

Create S3 Bucket and SQS Queue

```bash
aws-vault exec my-profile-name
aws s3api create-bucket --bucket my-bucket-name
aws sqs create-queue --queue-name my-queue-name
```
