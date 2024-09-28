import os

import boto3
from django.conf import settings
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="movies/", default="")
    filename = models.CharField(max_length=255, default="")
    filesize = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def file_path(self):
        return self.file.name

    def bucket_path(self):
        return os.path.join(self.file.storage.location, self.file_path())

    def get_presigned_url(self):
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )
        presigned_url = s3_client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                "Key": self.bucket_path(),
            },
            ExpiresIn=3600,  # URL expires in 1 hour
        )
        return presigned_url
