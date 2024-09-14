from django import forms
from django.contrib import admin

from .models import Movie
from .widgets import S3Boto3StorageFileInput


class MovieAdminForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "file": S3Boto3StorageFileInput,
        }


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
    form = MovieAdminForm
