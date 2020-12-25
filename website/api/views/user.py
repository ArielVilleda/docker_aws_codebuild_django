
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import serializers
from django.http import Http404

from api.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'status']


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField()

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'confirmation_token'
    lookup_url_kwarg = 'confirmation_token'

    def get_object(self, confirmation_token):
        try:
            return User.objects.get(confirmation_token=confirmation_token)
        except User.DoesNotExist:
            raise Http404

    @action(detail=True, methods=['post'])
    def set_password(self, request, confirmation_token=None):
        user = self.get_object(confirmation_token)
        p_serializer = PasswordSerializer(data=request.data)
        if p_serializer.is_valid():
            user.set_password(request.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(p_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
