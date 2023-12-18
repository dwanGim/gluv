from django.test import TestCase
from users.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

class TestUserCreate(TestCase):
    def setUp(self) -> None:
        # 테스트 시작 전에 호출되는 메서드
        return super().setUp()

    def tearDown(self) -> None:
        # 테스트 종료 후에 호출되는 메서드
        return super().tearDown()

    def test_create_user(self):
        # create_user 메서드를 사용하여 유저 생성 테스트
        user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            region='서울',
            nickname='test_nickname',
            is_active=True
        )

        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.region, '서울')
        self.assertEqual(user.nickname, 'test_nickname')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # create_superuser 메서드를 사용하여 슈퍼유저 생성 테스트
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            nickname='admin'
        )

        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_login_and_logout(self):

        login_data = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            region='서울',
            nickname='test_nickname',
            is_active=True
        )

        response = self.client.post('/users/login/', {'email': login_data.email, 'password': login_data.password}, format='json')

        if response.status_code == 200:
            self.assertIn('access', response.data)
            access_token = response.data['access']

            # 로그아웃
            logout_response = self.client.post('/users/logout/', {'refresh': access_token}, format='json')
            self.assertEqual(logout_response.status_code, 200)
            self.assertEqual(logout_response.data['detail'], 'Successfully logged out :D')
        else:
            error_message = response.data.get('detail', 'Unknown error :d')
            self.fail(f"Login failed with response: {error_message}")

        

class TokenRefreshTestCase(APITestCase):
    # 토큰 발급 및 검증 테스트 케이스
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            region='서울',
            nickname='testuser'
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)
        self.refresh_token = str(self.refresh)

    def test_refresh_token(self):
        response = self.client.post('/token/refresh/', {'refresh': self.refresh_token}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

        # # 토큰 검증 테스트케이스
        # verify_response = self.client.post(
        #     '/token/verify/',
        #     {'token': response.data['access']},
        #     content_type='application/json',
        #     HTTP_ACCEPT='application/json'
        # )

        # try:
        #     verify_response_data = verify_response.json()
        #     self.assertEqual(verify_response.status_code, 200)
        #     self.assertIn('token', verify_response_data)
        # except ValueError as e:
        #     print(f"에러 : JSON response : {e}")
        #     print(f"에러 내용 : content: {verify_response.content}")

    


class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            region='서울',
            nickname='testuser'
        )

    def test_user_profile_access(self):
        # 로그인
        login_response = self.client.post('/users/login/', {'email': 'test@example.com', 'password': 'testpassword'}, format='json')
        self.assertEqual(login_response.status_code, 200)

        # 로그인이 성공한 경우에만 토큰을 얻어옵니다.
        if login_response.status_code == 200:
            access_token = login_response.data.get('access')
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

            response = self.client.get(f'/users/{self.user.id}/profile/', format='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['nickname'], 'testuser')

    def test_user_profile_edit(self):
        # 로그인
        login_response = self.client.post('/users/login/', {'email': 'test@example.com', 'password': 'testpassword'}, format='json')
        self.assertEqual(login_response.status_code, 200)

        # 로그인이 성공한 경우에만 토큰을 얻어옵니다.
        if login_response.status_code == 200:
            access_token = login_response.data.get('access')
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

            data = {'nickname': 'updatednickname'}
            response = self.client.patch(f'/users/{self.user.id}/profile/', data, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['nickname'], 'updatednickname')

