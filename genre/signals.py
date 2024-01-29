from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify  import slugify

from .models import Genres

@receiver(pre_save, sender=Genres)
def genre_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        
            