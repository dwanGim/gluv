from django.test import TestCase
from users.models import User, CustomUserManager

class TestUserCreate(TestCase):
    def setUp(self) -> None:
        # 테스트 시작 전에 호출되는 메서드
        return super().setUp()

    def tearDown(self) -> None:
        # 테스트 종료 후에 호출되는 메서드
        return super().tearDown()
    
    print(User.object)
