from rest_framework import serializers

from .models import CommunityPost

class ListResponseSerializer(serializers.Serializer):
    '''
    일반적인 응답으로 포장하는 Serializer
    status : 응답 결과
    message : 응답 결과의 메시지
    data : 리스트 형태의 응답
    '''
    status = serializers.CharField()
    message = serializers.CharField()
    data = serializers.ListField(child=serializers.DictField())

class ResponseSerializer(serializers.Serializer):
    '''
    일반적인 응답으로 포장하는 Serializer
    status : 응답 결과
    message : 응답 결과의 메시지
    data : 단일 데이터 형태의 응답
    '''
    status = serializers.CharField()
    message = serializers.CharField()
    data = serializers.DictField()

class DetailSerializer(serializers.ModelSerializer):
    '''
    CommunityPost 모델에 대한 Serializer
    '''
    class Meta:
        model = CommunityPost
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    '''
    Content를 제외한 Serializer
    '''
    class Meta:
        model = CommunityPost
        exclude = ['content']

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
