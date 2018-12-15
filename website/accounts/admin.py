from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class StudentInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'
    extra = 0

class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
