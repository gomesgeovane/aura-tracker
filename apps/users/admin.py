from django.contrib import admin
from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    readonly_fields = ('id',)
    search_fields = ('username', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user__id', 'user__username', 'aura', 'created_at')
    readonly_fields = ('id',)
    search_fields = ('user__username',)