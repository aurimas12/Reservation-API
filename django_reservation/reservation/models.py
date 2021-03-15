from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(verbose_name="Title", max_length=64)
    start_time = models.CharField(verbose_name="Meeting start", max_length=64)
    end_time = models.CharField(verbose_name="Meeting end", max_length=64)
    date = models.CharField(verbose_name="Meeting date", max_length=64)
    employees = models.IntegerField(verbose_name="Employees")


# @reveiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,isntance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)
