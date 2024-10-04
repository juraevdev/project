from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Book

@receiver(post_save, sender=Book)
def set_slug(sender, instance, created, **kwargs):
    if created and not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()

@receiver(pre_save, sender=Book)
def check_for_updates(sender, instance, **kwargs):
    print('Duplicate entry found')
    if Book.objects.filter(name=instance.name).exists():
        raise ValueError('Duplicate entry found')