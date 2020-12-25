from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Admin(AbstractUser):
    class Meta:
        verbose_name = _('Admin')
        verbose_name_plural = _('Admins')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
