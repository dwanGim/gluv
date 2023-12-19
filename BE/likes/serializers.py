# serializers.py
from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'community_post', 'recruitment_post']

# 또는 필요한 필드만 선택적으로 포함할 수 있습니다.
# fields = ['user', 'community_post']  # 또는 'recruitment_post' 등
