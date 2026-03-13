from django.db import models
from django.core.exceptions import ValidationError

def validator_is_zero(value:int):
    if value == 0:
        raise ValidationError('Aura transaction cannot be zero. Use positive values for rewards and negative for penalties.')

class Transaction(models.Model):
    sender = models.ForeignKey('users.Profile', models.SET_NULL, null=True, related_name='sent_transactions', verbose_name='Sender')
    recipient = models.ForeignKey('users.Profile', models.CASCADE, related_name='received_transactions', verbose_name='Recipient')
    aura = models.IntegerField('Aura', validators=[validator_is_zero])
    reason = models.CharField('Reason', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()

        if self.sender_id and self.sender_id == self.recipient_id:
            raise ValidationError({'recipient': 'Self-promotion detected! You cannot send Aura to your own profile.'})

    def __str__(self):
            sender = self.sender.user.username if self.sender else 'Deleted User'
            recipient = self.recipient.user.username
            sign = '+' if self.aura > 0 else ''

            return f'{sender} ({sign}{self.aura}) -> {recipient}'