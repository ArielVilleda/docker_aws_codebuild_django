from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password


class User(models.Model):
    class UserStatus(models.TextChoices):
        PAYMENT_VALIDATION = ('payment_validation', _('PAYMENT_VALIDATION'))
        HAS_LATE_PAYMENT = ('has_late_payment', _('HAS_LATE_PAYMENT'))
        BANNED = ('banned', _('BANNED'))
        NORMAL = ('normal', _('NORMAL'))

    class Meta:
        indexes = [
            models.Index(fields=['confirmation_token']),
            models.Index(fields=['email'])
        ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, default="0000000000")
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=50)
    email_verified_at = models.DateTimeField(null=True)
    confirmation_token = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        null=False,
        blank=False,
        default=UserStatus.PAYMENT_VALIDATION
    )

    def set_password(self, password):
        self.password = make_password(password)
        self.confirmation_token = None
        self.save()
        return self

    @staticmethod
    def make_confirmation_token(length=64):
        return get_random_string(length)

    def assign_confirmation_token(self):
        self.confirmation_token = self.make_confirmation_token()
        self.save()
        return self
