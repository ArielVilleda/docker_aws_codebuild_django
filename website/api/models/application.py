from datetime import datetime
from django.db import models

from .payment_plan import PaymentPlan
from .user import User
from .domain import Domain
from .commerce_template import CommerceTemplate


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, null=True, on_delete=models.SET_NULL)
    commerce_template = models.ForeignKey(CommerceTemplate, null=True,
                                          on_delete=models.SET_NULL)
    payment_plan = models.ForeignKey(PaymentPlan, null=True,
                                     on_delete=models.SET_NULL)
    paid = models.DecimalField(null=False, max_digits=10, decimal_places=2,
                               default=0)
    paid_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
