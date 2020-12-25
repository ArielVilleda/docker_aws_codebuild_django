from rest_framework import serializers

from api.models.commerce_template import CommerceTemplate


class CommerceTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommerceTemplate
        fields = ['id', 'name', 'thumbnail', 'url']
