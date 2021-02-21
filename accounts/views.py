from django.shortcuts import render
from accounts.forms import UserRegistrationForm
from django.views import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from accounts.tokens import activation
from accounts.models import User
from django.db.transaction import atomic

# Create your views here.
class UserReistrationView(View):
    def get(self, request, *args, **kwargs):
        template_name = "accounts/signup.html"
        form = UserRegistrationForm()
        return render(request, template_name, {"form": form})
    @atomic
    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user_email = form.cleaned_data['email']
            email_html_template = "accounts/activation_template.html"
            email_subject = "Please activate your account"
            template = render_to_string(
                email_html_template,
                {
                    "domain": request.get_host(),
                    "uid" : urlsafe_base64_encode(force_bytes(user.id)),
                    "token": activation.make_token(user)
                })
            email = EmailMessage(email_subject, template, to=[user_email])
            email.content_subtype = "html"
            email.send()
            template_name = "accounts/success.html"
            return render(request, template_name, {"form": form})
        else:
            template_name = "accounts/signup.html"
            return render(request, template_name, {"form": form})

        
        

def activate_email(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    try:
        user = User.objects.get(pk=uid)
        activation.check_token(user, token)
        user.is_active = True
        user.save()
    except (User.DoesNotExist, Exception):
        pass

