from django.contrib import admin
from apps.user.models import Role, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Role)
admin.site.register(User, UserAdmin)
