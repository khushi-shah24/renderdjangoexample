# signals.py

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Post
import cloudinary

@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        # Extract the public ID from the Cloudinary URL
        public_id = instance.image.public_id
        # Delete the image from Cloudinary
        cloudinary.uploader.destroy(public_id, resource_type='image')
