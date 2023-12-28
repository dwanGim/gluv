from rest_framework import serializers

from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'community_post', 'recruitment_post']

