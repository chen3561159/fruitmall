from django.db import models
from  myadmin.adminmanager.models import manager
# Create your models here.
class Userinfo(models.Model):
    name=models.CharField(max_length=20)
    pwd=models.CharField(max_length=40)
    phone=models.IntegerField(null=True)
    question=models.CharField(max_length=250)
    answer=models.CharField(max_length=100)
    mid=models.ForeignKey("adminmanager.manager",null=True,blank=True,on_delete=models.SET_NULL)

