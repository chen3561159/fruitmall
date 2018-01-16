from django.db import models
from myadmin.menu.models import  Menumessage
# Create your models here.
class manager(models.Model):
    name=models.CharField(max_length=150)
    privall=models.ManyToManyField("menu.Menumessage")