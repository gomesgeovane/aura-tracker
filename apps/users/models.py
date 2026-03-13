from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
from django.core.validators import RegexValidator

class User(AbstractUser):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]+$', 'Only letters, numbers and underscores are allowed.')

    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
    email = models.EmailField('E-Mail', unique=True)
    username = models.CharField('Username', max_length=50, unique=True, validators=[alphanumeric])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile', verbose_name='User')
    picture = models.ImageField('Picture', upload_to='profiles/pictures/', blank=True, null=True)
    bio = models.TextField('Biography', max_length=255, blank=True)
    aura = models.IntegerField('Aura', default=0)
    created_at = models.DateField('Created at', auto_now_add=True)

    def __str__(self):
        return self.user.username