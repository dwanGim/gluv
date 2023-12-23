from rest_framework import serializers

from likes.models import Like
from .models import CommunityPost


class DetailSerializer(serializers.ModelSerializer):
    '''
    CommunityPost 모델에 대한 Serializer
    '''
    likes = serializers.SerializerMethodField()
    class Meta:
        model = CommunityPost
        fields = '__all__'
    
    def get_likes(self, obj):
        '''
        추천수 조회
        '''
        return Like.objects.filter(community_post=obj.id).count()


class SummarySerializer(serializers.ModelSerializer):
    '''
    Content를 제외한 Serializer
    '''
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = CommunityPost
        exclude = ['content']
        

    def get_nickname(self, obj):
        return obj.author.nickname
    

class IDOnlySerializer(serializers.ModelSerializer):
    '''
    ID 필드만 포함하는 Serializer
    '''
    post_id = serializers.IntegerField(source='id')

    class Meta:
        model = CommunityPost
        fields = ['post_id']


class CreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    category = serializers.ChoiceField(choices=[
            "notice", "qna", "creation-novel", "creation-poem", 
            "creation-essay", "comm-novel", "comm-poem", "comm-essay"
        ], required=True)


class ModifyRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    category = serializers.ChoiceField(choices=[
            "notice", "qna", "creation-novel", "creation-poem", 
            "creation-essay", "comm-novel", "comm-poem", "comm-essay"
        ], required=False)
