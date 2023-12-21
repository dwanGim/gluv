from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user_id', 'recruit_id', 'post_id', 'content', 'to_user', 'created_at', 'updated_at')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post_id', 'recruit_id', 'to_user')
