from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Role(models.Model):
    AUTHOR = 1
    AUDITOR = 2
    ADMIN = 3
    VISITOR = 4
    ROLE_CHOICES = (
        (AUTHOR, "Author"),
        (AUDITOR, "Auditor"),
        (ADMIN, "Admin"),
        (VISITOR, "Visitor")
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key =True)

    def __str__(self):
        return self.get_id_display()
    


class User(AbstractUser):
    role = models.ManyToManyField(Role)
    avatar = models.ImageField(blank=True, null=True)
    email = models.EmailField(
        _('email'),
        max_length=150,
        unique=True,
        help_text=_('Required. Enter valid email.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    REQUIRED_FIELDS= ["email", "first_name", "last_name"]
    
    def __str__(self):
        return self.email
    