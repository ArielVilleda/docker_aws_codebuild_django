from django.db import models


class CommerceTemplate(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='public_images/commerce_template/')
    enabled = models.BooleanField(default=True)
    url = models.CharField(max_length=255, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
