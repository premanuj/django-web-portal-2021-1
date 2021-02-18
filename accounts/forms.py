from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("first_name", "last_name", "username", "email")
