from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    filesize = models.IntegerField(default=0)
    width = models.IntegerField()
    height = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title
