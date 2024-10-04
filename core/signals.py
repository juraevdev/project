from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Book
import logging

logger = logging.getLogger(__name__)

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
    
@receiver(pre_delete, sender=Book)
def log_before_delete(sender, instance, **kwargs):
    logger.info(f"The book '{instance.name}' is about to be deleted.")