from rest_framework import serializers
from .models import RecruitmentPost

class RecruitmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentPost
        fields = '__all__'
