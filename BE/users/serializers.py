from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    '''
    User 모델 Serializer
    '''
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'created_at', 'region', 'nickname', 'profile_image', 'profile_content', 'is_blocked')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not instance.profile_image:
            ret['profile_image'] = '/media/default_profile.png'
        return ret


class UserEditSerializer(serializers.ModelSerializer):
    '''
    User 모델 수정을 위한 Serializer
    '''
    class Meta:
        model = User
        fields = ('region', 'nickname', 'profile_image', 'profile_content')

class UserVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password')

class UserSummarySerializer(serializers.ModelSerializer):
    '''
    댓글, 게시글 등 유저 정보 요약을 위한 Serializer
    '''
    class Meta:
        model = User
        fields = ('id', 'nickname', 'profile_image')
