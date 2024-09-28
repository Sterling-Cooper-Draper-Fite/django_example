from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver

from .models import Movie


def register_signals():
    @receiver(post_delete, sender=Movie)
    def delete_associated_files(sender, instance, **kwargs):
        if instance.file:
            instance.file.delete(save=False)

    @receiver(pre_save, sender=Movie)
    def store_old_file_path(sender, instance, **kwargs):
        if not instance.pk:
            return

        try:
            old_instance = Movie.objects.get(pk=instance.pk)
            instance._old_file = old_instance.file
        except Movie.DoesNotExist:
            instance._old_file = None

    @receiver(post_save, sender=Movie)
    def delete_old_file_on_change(sender, instance, **kwargs):
        if hasattr(instance, "_old_file") and instance._old_file:
            old_file = instance._old_file
            new_file = instance.file

            if old_file and old_file != new_file:
                old_file.delete(save=False)
