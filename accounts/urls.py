
from django.urls import path
from accounts.views import UserReistrationView, activate_email
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', UserReistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('activate/<uidb64>/<token>/', activate_email, name='activation')
]
