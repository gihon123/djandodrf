from django.contrib import admin

# Register your models here.

from apps.users.models import UsersModel

class UsersModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(UsersModel, UsersModelAdmin)
