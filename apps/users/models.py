from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
from django.core.validators import RegexValidator

class User(AbstractUser):
    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
    email = models.EmailField('E-Mail', unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Profile(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]+$', 'Only letters, numbers and underscores are allowed.')

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile', verbose_name='User')
    picture = models.ImageField('Picture', upload_to='profiles/pictures/', blank=True, null=True)
    username = models.CharField('Username', max_length=50, unique=True, validators=[alphanumeric])
    bio = models.TextField('Biography', max_length=255, blank=True)
    aura = models.IntegerField('Aura', default=0)

    def __str__(self):
        return self.username