from django.db import models
from .user import User
from .category import Category


class Store(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='public_images/store/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
