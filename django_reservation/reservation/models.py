from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Meeting(models.Model):
    title = models.CharField(verbose_name="Title", max_length=64)
    start_time = models.CharField(verbose_name="Meeting start", max_length=64)
    end_time = models.CharField(verbose_name="Meeting end", max_length=64)
    date = models.CharField(verbose_name="Meeting date", max_length=64)
    employees = models.IntegerField(verbose_name="Employees")


class User(AbstractUser):
    email = models.EmailField(
        max_length=255, verbose_name='email', unique=True)
    phone = models.EmailField(max_length=255, null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    USERNAME_FIELD = 'email'

    def get_usename(self):
        return self.email
