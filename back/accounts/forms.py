from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# custom을 하는 이유: 기존의 userform은 제한적임 
from django.contrib.auth import get_user_model
# get_user_model: 유효성 검사후 로그인/비 로그인 확인

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name','email',)