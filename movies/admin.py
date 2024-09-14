from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "file",
        "filename",
        "filesize",
        "width",
        "height",
        "duration",
    )
    search_fields = ("title", "filename")
