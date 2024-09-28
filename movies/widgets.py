from django.forms.widgets import ClearableFileInput


class S3Boto3StorageFileInput(ClearableFileInput):
    template_name = "forms/widgets/clearable_file_input.html"

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if value and hasattr(value, "url"):
            context["widget"]["initial_url"] = value.instance.file.url
        return context
