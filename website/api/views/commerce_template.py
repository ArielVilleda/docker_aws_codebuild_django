from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models.commerce_template import CommerceTemplate
from api.serializers import CommerceTemplateSerializer


class CommerceTemplateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CommerceTemplate.objects.all()
    serializer_class = CommerceTemplateSerializer
    permission_classes = [AllowAny]
