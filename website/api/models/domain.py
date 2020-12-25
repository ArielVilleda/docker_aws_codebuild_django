from django.db import models
from .store import Store


class Domain(models.Model):
    path = models.CharField(max_length=100, null=False, blank=False,
                            unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)