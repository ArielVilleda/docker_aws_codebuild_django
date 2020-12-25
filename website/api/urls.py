from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'commerce-template', views.CommerceTemplateViewSet)
router.register(r'lead', views.LeadViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = router.urls
