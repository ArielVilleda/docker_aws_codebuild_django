from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from api.models.lead import Lead

# TEST
import os
ENV_MSG_TEST = os.environ.get('ENV_MSG_TEST', 'Nothing read in env :(')


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['email', 'domain', 'current_application_step', 'category',
                  'additional_data']


class LeadViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]
    lookup_field = 'email'
    lookup_url_kwarg = 'email'
    lookup_value_regex = r'[\w@.]+'

    # def list(self, request):
    #     queryset = Lead.objects.all()
    #     serializer = LeadSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = LeadSerializer(instance=instance)
    #     return Response(serializer.data)

    def create(self, serializer):
        # parsing data
        data = self.request.data
        parsed_data = {
            'email': data.pop('email', None),
            'domain': data.pop('domain', None),
            'category': data.pop('category', None),
            'current_application_step': data.pop('current_application_step',
                                                 None)
        }
        parsed_data['additional_data'] = data
        serializer = LeadSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
