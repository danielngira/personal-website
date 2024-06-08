from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import datetime

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Project(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+1)]
    name = models.TextField
    description = models.TextField
    year = models.IntegerField(('year'), choices = YEAR_CHOICES, default = datetime.datetime.now().year)
