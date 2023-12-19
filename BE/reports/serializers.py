from rest_framework import serializers
from .models import Report

class CreateReportSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    content = serializers.CharField(required=True)

class ReportSerializer(serializers.Serializer):
    '''
    Report 모델 Serializer
    '''
    class Meta:
        model = Report
        fields = '__all__'
