from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'created_at', 'region', 'nickname', 'profile_image', 'profile_content', 'is_blocked')
        # extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not instance.profile_image:
            ret['profile_image'] = '/media/default_profile.png'  # 기본 이미지의 경로
        return ret


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('region', 'nickname', 'profile_image', 'profile_content')
