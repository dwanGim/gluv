from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreateForm(UserCreationForm):
    '''
    회원가입 폼
    '''
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','nickname']
