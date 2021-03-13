from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(verbose_name="Title", max_length=64)
    start_time = models.CharField(verbose_name="Meeting start", max_length=64)
    end_time = models.CharField(verbose_name="Meeting end", max_length=64)
    date = models.CharField(verbose_name="Meeting date", max_length=64)
    employees = models.IntegerField(verbose_name="Employees")
