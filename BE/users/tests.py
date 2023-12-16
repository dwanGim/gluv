from django.test import TestCase
from users.models import User

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
            region='test_region',
            nickname='test_nickname'
        )

        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.region, 'test_region')
        self.assertEqual(user.nickname, 'test_nickname')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # create_superuser 메서드를 사용하여 슈퍼유저 생성 테스트
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword'
        )

        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
