from django.contrib import admin
from accounts.models import User, Role
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', "username", "last_login")

admin.site.register(Role)

