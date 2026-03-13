from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'aura', 'created_at')
    search_fields = ('sender__user__username', 'recipient__user__username', 'reason')
    search_fields = ('sender', 'recipient')

    def get_readonly_fields(self, request, obj=None):
            if obj:
                return ('sender', 'recipient', 'aura', 'reason', 'created_at')
            return ('created_at',)