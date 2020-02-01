from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'slug',
            'profile_pic',
            'is_active',
            'is_staff',
            'user_updated',
            'user_created', ]

        read_only_fields = [
            'id',
            'slug',
            'is_active',
            'is_staff',
            'user_updated',
            'user_created',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password', 'placeholder': 'Password'}
            }
        }

    def create(self, validated_data):
        """From rest framework user creation and token creation will came here"""
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user, key=user.slug)
        return user
