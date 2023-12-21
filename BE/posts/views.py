from collections import OrderedDict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import pagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.db import transaction, models

from posts.models import CommunityPost
from posts.serializers import CreateRequestSerializer, DetailSerializer, IDOnlySerializer, ModifyRequestSerializer, SummarySerializer

class CommunityPostPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, status, message, data):
        return Response(OrderedDict([
            ('status', 'success'),
            ('message', 'Success message'),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
    
class CommunityPostView(viewsets.ViewSet):
    '''
    커뮤니티 게시글 관련 ViewSet
    '''
    pagination_class = pagination.PageNumberPagination
    serializer_class = DetailSerializer

    def get_permissions(self):
        # list, notices, hot, retrieve 메서드에는 권한 필요 없음
        if self.action in ['list', 'notices', 'hot', 'retrieve']:
            return [AllowAny()]
        
        # partial_update, delete 메서드는 요청자와 작성자가 동일한지 체크
        if self.action in ['partial_update', 'delete']:
            return [IsAuthenticated()]
        # 기타 경우에는 기본 권한 적용
        else:
            return [IsAuthenticated()]
    
    def has_object_permission(self, request, post):
        return post.author == request.user
    
    def generate_response(self, status, message, data=None):
        return {
            'status': status,
            'message': message,
            'data': data,
        }
    
    @action(methods=["get"], detail=False, url_path='notices', url_name="notices")
    def notices(self, request, *args, **kwargs):
        '''
        공지 사항을 조회하는 함수
        '''
        paginator = CommunityPostPagination()
        notices = CommunityPost.objects.filter(category='notice')
        page = paginator.paginate_queryset(notices, request)
        serializer = SummarySerializer(page, many=True)
        return paginator.get_paginated_response(status='success', message='Successfully', data=serializer.data)
    
    def list(self, request, *args, **kwargs):
        '''
        특정 조건에 따라 게시글 목록 조회
        '''

        # 필터링 조건 파싱
        search_query = request.GET.get('search', '')
        category_query = request.GET.getlist('category', [])
        author_query = request.GET.get('author', '')
        order_by_query = request.GET.get('order_by', 'created_at')
        order_query = request.GET.get('order', 'asc')
        
        # 필터링 조건 설정
        filter_conditions = {}

        # 제목 검색
        if search_query:
            filter_conditions['title__icontains'] = search_query

        # 커뮤니티 게시판만 검색
        if 'creation' in category_query:
            filter_conditions['category__startswith'] = 'creation'
        # 커뮤니티 게시판만 검색
        elif 'comm' in category_query:
            filter_conditions['category__startswith'] = 'comm' 
        # 다중 카테고리 선택 검색
        elif category_query:
            filter_conditions['category__in'] = category_query

        # 작성자 검색
        if author_query:
            filter_conditions['author__nickname'] = author_query

        # 정렬 기준
        order = 'created_at'
        if order_by_query.lower() == 'views':
            order = 'view_count'

        # 정렬 순서 
        if order_query.lower() == 'asc':
            order = order
        else:
            order = '-' + order
        

        paginator = CommunityPostPagination()
        posts = CommunityPost.objects.exclude(category='notice').filter(**filter_conditions).order_by(order)
        page = paginator.paginate_queryset(posts, request)
        serializer = SummarySerializer(page, many=True)
        return paginator.get_paginated_response(status='success', message='Successfully', data=serializer.data)
    
    @action(methods=["get"], detail=False, url_path='hot', url_name="hot")
    def hot(self, request, *args, **kwargs):
        '''
        인기 게시글 검색
        '''
        paginator = CommunityPostPagination()
        post = CommunityPost.objects.exclude(category='notice').order_by('-view_count')
        page = paginator.paginate_queryset(post, request)
        serializer = SummarySerializer(page, many=True)
        return paginator.get_paginated_response(status='success', message='Successfully', data=serializer.data)
    
    @transaction.atomic
    def retrieve(self, request, pk=None, *args, **kwargs):
        '''
        게시글 상세 조회
        '''
        try:
            post = CommunityPost.objects.get(id=pk)
            response = self.generate_response(
                status='success',
                message = 'Success message',
                data = DetailSerializer(post, many=False).data
            )
            post.view_count = models.F('view_count') + 1
            post.save()
            return Response(status=status.HTTP_200_OK, data=response)
        except Exception as e:
            response = self.generate_response(
                status='fail',
                message = str(e),
            )
            return Response(status=status.HTTP_200_OK, data=response)


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='Authorization',
                location=OpenApiParameter.HEADER,
                type=str,
                description='JWT 토큰 (Bearer 헤더 사용)',
                required=True,
            ),
        ],
        request=CreateRequestSerializer
    )
    def create(self, request, *args, **kwargs):
        data = request.data

        title = data.get('title')
        category = data.get('category')
        content = data.get('content')

        response = {
            'status': 'success',
            'message': 'Success message',
            'data': None,
        }

        try:
            post = CommunityPost(
                title=title,
                content=content,
                category = category,
                author = request.user,
            )
            post.save()
            response['data'] = IDOnlySerializer(post, many=False).data
        except Exception as e:
            response['status'] = 'fail'
            response['message'] = f'{str(e)}'

        response = self.generate_response(**response)
        return Response(status=status.HTTP_200_OK, data=response)
    
    @extend_schema(
        request=ModifyRequestSerializer
    )
    def partial_update(self, request, pk=None, *args, **kwargs):
        response = {
            'status': 'success',
            'message': 'Success message',
        }
        print(request.user)
        
        try:
            post = CommunityPost.objects.get(id=pk)
            # 나중에 리팩토링 해야함.
            is_author = self.has_object_permission(request=request, post=post)
            if is_author is False:
                response['status'] = 'UNAUTHORIZED'
                response['message'] = '게시글 작성자가 아닙니다.'
            else:
                serializer = DetailSerializer(post, data=request.data, partial=True)
                serializer.is_valid(raise_exception=False)
                serializer.save()
        except CommunityPost.DoesNotExist:
            response['status'] = 'NOT_FOUND'
            response['message'] = '게시글을 찾을 수 없습니다.'
        except Exception as e:
            response['status'] = 'error'
            response['message'] = str(e)

        response = self.generate_response(**response)
        return Response(status=status.HTTP_200_OK, data=response)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        response = {
            'status': 'success',
            'message': 'Success message',
        }

        try:
            post = CommunityPost.objects.get(id=pk)
            is_author = self.has_object_permission(request=request, post=post)

            if not is_author:
                response['status'] = 'UNAUTHORIZED'
                response['message'] = '게시글 작성자가 아닙니다.'
            else:
                post.delete()
        except CommunityPost.DoesNotExist:
            response['status'] = 'NOT_FOUND'
            response['message'] = '게시글을 찾을 수 없습니다.'
        except Exception as e:
            response['status'] = 'error'
            response['message'] = str(e)

        response = self.generate_response(**response)
        return Response(status=status.HTTP_200_OK, data=response)