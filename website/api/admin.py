from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models.application import Application
from api.models.category import Category
from api.models.commerce_template import CommerceTemplate
from api.models.domain import Domain
from api.models.lead import Lead
from api.models.payment_plan import PaymentPlan
from api.models.store import Store
from api.models.user import User
from api.models.admin import Admin

admin.site.register(Admin, UserAdmin)
admin.site.register([
     Application,
     Category,
     CommerceTemplate,
     Domain,
     Lead,
     PaymentPlan,
     Store,
     User
])
