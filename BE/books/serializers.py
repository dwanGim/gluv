from rest_framework import serializers

from .models import Book

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

class BookSerializer(serializers.ModelSerializer):
    '''
    Book 모델에 대한 Serializer로 'id' 필드를 제외함
    '''
    class Meta:
        model = Book
        exclude = ['id']
