from django.shortcuts import render

# Create your views here.
'''
요구사항 :
1. 본인 게시글에는 좋아요 누를 수 없도록 (토의 필요)
2. 이미 like 한 게시글에 like 요청 시 에러 반환 (마찬가지로 like 하지 않은 글에 대해 unlike 시 에러 반환)
3. 로그인 한 사용자만 사용 가능
4. 좋아요 할 수 있는 대상은 커뮤니티 게시글, 모집 게시글
'''