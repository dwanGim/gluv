from rest_framework import serializers

from .models import Comment
from users.serializers import UserSummarySerializer


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    user = UserSummarySerializer(source='user_id')
    to_user_info = UserSummarySerializer(source='to_user')
    
    class Meta:
        model = Comment
        fields = ('user_id', 'recruit_id', 'post_id', 'content', 
                    'to_user', 'created_at', 'updated_at', 'nickname', 'user', 'to_user_info')
        
        
    def get_nickname(self, obj):
        '''
        닉네임 정보 제공
        '''
        return obj.user_id.nickname

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post_id', 'recruit_id', 'to_user')
