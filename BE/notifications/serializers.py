from rest_framework import serializers

from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    '''
    Notification 모델에 대한 Serializer
    '''
    class Meta:
        model = Notification
        fields = '__all__'

class ReadNotificationSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())