
from django.urls import path
from accounts.views import UserReistrationView

urlpatterns = [
    path('register', UserReistrationView.as_view(), name='register'),
    
]
