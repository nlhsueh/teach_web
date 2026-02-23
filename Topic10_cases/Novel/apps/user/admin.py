from django.contrib import admin
from .models import User, Subscribe

class UserAdmin(admin.ModelAdmin):
    list_display = ("account", "username")

admin.site.register(User, UserAdmin)
admin.site.register(Subscribe)
