from django.contrib import admin
from apps.user.models import Role, User
# Register your models here.
admin.site.register(Role)
admin.site.register(User)
