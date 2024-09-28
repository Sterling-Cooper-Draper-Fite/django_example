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
