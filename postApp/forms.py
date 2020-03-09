from django.contrib.auth.forms import UserCreationForm
from postApp.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "profile_pic")
