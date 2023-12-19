from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from reports.serializers import CreateReportSerializer, ReportSerializer
from django.contrib.auth import get_user_model

from reports.models import Report

User = get_user_model()

@extend_schema_view(
    create=extend_schema(
        request=CreateReportSerializer(),
        responses={201: ReportSerializer}
    )
)
class ReportView(viewsets.ViewSet):
    '''
    신고 관련 ViewSet
    '''

    def get_permissions(self):
        return [IsAuthenticated()]
    
    def generate_response(self, status, message, data=None):
        return {
            'status': status,
            'message': message,
        }
    
    def create(self, request, *args, **kwargs):
        '''
        신고 API
        '''
        serializer = CreateReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = serializer.validated_data.get('user_id', '')
        reported_user = User.objects.get(id=user_id)
        report = Report.objects.create(
            reporting_user=request.user,
            reported_user=reported_user,
            content=serializer.validated_data['content']
        )

        response = self.generate_response(
            status='success',
            message='성공적으로 신고했습니다.'
        )
        return Response(status=status.HTTP_201_CREATED, data=response)
    