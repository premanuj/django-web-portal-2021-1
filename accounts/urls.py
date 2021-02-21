
from django.urls import path
from accounts.views import UserReistrationView, activate_email

urlpatterns = [
    path('register/', UserReistrationView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', activate_email, name='activation')
]
