from django.db import models

from .category import Category


class Lead(models.Model):
    class Meta:
        indexes = [models.Index(fields=['email'])]

    email = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    current_application_step = models.IntegerField(default=0)
    additional_data = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
