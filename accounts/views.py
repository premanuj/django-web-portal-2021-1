from django.shortcuts import render
from accounts.forms import UserRegistrationForm
from django.views import View

# Create your views here.
class UserReistrationView(View):
    def get(self, request, *args, **kwargs):
        template_name = "accounts/signup.html"
        form = UserRegistrationForm()
        return render(request, template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
