from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Like, CommunityPost, RecruitmentPost
from teams.models import Team

class LikeModelTest(TestCase):
    '''
    좋아요 모델 테스트

    Detail:
        커뮤니티 게시글, 모집 게시글에 대한 좋아요 요청
        1~2. 각각 요청시 성공했는지 확인
        3. 오류로 인해 커뮤니티 게시글, 모집 게시글 id가 동시에 들어갔을 때에 대한 오류 확인
        4. 이미 Like 되어있는 게시글에 대한 post요청 오류 확인
    '''
    def setUp(self) -> None:
        # 유저 생성
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpw111',
            region='test',
            nickname='TestUser'
        )
        # 유저2 생성(게시글 작성자)
        self.user2 = get_user_model().objects.create_user(
            email='testuser2@example.com',
            password='testpw222',
            region='test',
            nickname='TestUser2'
        )

        # 커뮤니티 게시글 생성
        self.community_post = CommunityPost.objects.create(
            author=self.user2,
            title='Community Test',
            category='notice',
            content='CommunityPost Test'
        )

        # 팀 생성
        self.team = Team.objects.create(
            name='TestTeam',
            category='독서모임',
            is_closed=False,
            location='Test',
            max_attendance=10,
            current_attendance=0,
            introduce='Test',
            image=None
        )
        # 모집 게시글 생성
        self.recruitment_post = RecruitmentPost.objects.create(
            team=self.team,
            author=self.user2,
            title='Recruitment Test',
            content='RecruitmentPost Test'
        )

        self.client.force_login(self.user)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_like_community_post(self):
        # 커뮤니티 게시글 좋아요 테스트
        
        # 커뮤니티 게시글에 대한 좋아요 POST 요청 응답 확인
        response = self.client.post('/like/', {'post_id': self.community_post.id})
        self.assertEqual(response.status_code, 200)

        # like가 생성되었는지 확인
        like = Like.objects.get(user=self.user, community_post=self.community_post)
        self.assertIsNotNone(like)
        self.assertEqual(like.recruitment_post, None)

    def test_like_recruitment_post(self):
        # 모집 게시글 좋아요 테스트
        
        # 모집 게시글에 대한 좋아요 POST 요청 응답 확인
        response = self.client.post('/like/', {'recruit_id': self.recruitment_post.id})
        self.assertEqual(response.status_code, 200)

        # like가 생성되었는지 확인
        like = Like.objects.get(user=self.user, recruitment_post=self.recruitment_post)
        self.assertIsNotNone(like)
        self.assertEqual(like.community_post, None)

    def test_like_both_post(self):
        # 모집 게시글, 커뮤니티 게시글의 id가 전부 POST요청에 들어갔을 때

        # 잘못된 요청에 대한 좋아요 POST 응답 반환
        response = self.client.post('/like/', {'recruit_id': self.recruitment_post.id, 'community_post_id': self.community_post.id})
        self.assertEqual(response.status_code, 400)

        # 잘못된 요청에 대해 like객체가 생성되지 않았음을 확인
        # 모집 게시글에 대한 좋아요 생성 확인
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(user=self.user, recruitment_post=self.recruitment_post)
        # 커뮤니티 게시글에 대한 좋아요 생성 확인
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(user=self.user, community_post=self.community_post)

    def test_like_double_post(self):
        # 같은 게시글에 두번 POST요청을 했을 때

        # 첫 번째 좋아요
        response1 = self.client.post('/like/', {'post_id': self.community_post.id})
        self.assertEqual(response1.status_code, 200)

        # 두 번째 좋아요 시도
        response2 = self.client.post('/like/', {'post_id': self.community_post.id})
        # 중복해서 좋아요를 누르면 에러 반환
        self.assertEqual(response2.status_code, 400)
        
        # 해당 게시글에 대한 like가 추가로 생성된 것은 아닌지 확인
        like_count = Like.objects.filter(user=self.user, community_post=self.community_post).count()
        self.assertEqual(like_count, 1)