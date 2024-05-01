from django.contrib import admin
from .models import CustomUser, Role, UserLog, UserRole
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(UserLog)
admin.site.register(UserRole)