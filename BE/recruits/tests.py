from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import RecruitmentPost

from schedules.models import Schedule
from teams.models import Team, TeamMember


class TestRecruitmentPostModel(TestCase):
    '''
    모집 게시글 모델 테스트

    Detail:
        모집 게시글 생성 요청 테스트
        1. 모집 게시글 생성 시 모임, 일정까지 생성되었는지 확인
        2. 모집 게시글 생성 후 타 유저가 신청
    '''

    def setUp(self) -> None:
        # 유저 생성
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpw111',
            region='test',
            nickname='TestUser'
        )

        self.client.force_login(self.user)

        self.request_set = {'title': 'test_title', 'content': 'Test content', 'category': '독서모임', 'max_attendance':5, 'leader_id' : self.user.id, 'frequency':'매달', 'week': '세번째', 'day':'월요일, 수요일'}

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_create_recruitment_post(self):
        # request body로 날아온 data 분할해서 사용
        # 팀 생성
        team = Team.objects.create(name='TestTeam', category='독서모임', max_attendance=10)
        team_id = team.id

        # 모집 게시글 생성
        recruitment_post = self.client.post('/recruits/', {'title': self.request_set['title'], 'content': self.request_set['content']})
        post_id = recruitment_post.data['id']

        # 일정 생성
        schedule = Schedule.objects.create(team_id=team_id, frequency=self.request_set['frequency'], week=self.request_set['week'], day=self.request_set['day'])
        schedule_id = schedule.id

        # 생성된 모임, 일정, 게시글 확인
        team_exists = Team.objects.filter(id=team_id).exists()
        schedule_exists = Schedule.objects.filter(id=schedule_id).exists()
        post_exists = RecruitmentPost.objects.filter(id=post_id).exists()

        self.assertTrue(team_exists)
        self.assertTrue(schedule_exists)
        self.assertTrue(post_exists)

def test_apply_recruitment_post(self):
        # 팀 생성
        team = Team.objects.create(name='TestTeam', category='독서모임', max_attendance=10)
        team_id = team.id

        # 모집 게시글 생성
        recruitment_post = self.client.post('/recruits/', {'title': self.request_set['title'], 'content': self.request_set['content']})
        post_id = recruitment_post.data['id']

        # 다른 유저 생성
        user2 = get_user_model().objects.create_user(
            email='testuser2@example.com',
            password='testpw222',
            region='test',
            nickname='TestUser2'
        )

        # 유저2가 모집 게시글에 가입신청
        response_apply = self.client.post(f'/recruits/{post_id}/apply/', {'user_id': user2.id})
        self.assertEqual(response_apply.status_code, 200)  
        # 가입신청 후 TeamMember 확인
        team_member_exists = TeamMember.objects.filter(user=user2, team_id=team_id, is_approved=False).exists()
        self.assertTrue(team_member_exists)