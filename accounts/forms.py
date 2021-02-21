from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from accounts.models import User
from django.forms import Form

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "avatar")
    
    def clean_email(self):
        value = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=value)
            if user:
                raise ValueError("Email already exist.")
        except Exception as e:
            pass
        return value

            
