# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Userinfo(models.Model):
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=40)
    phone=models.IntegerField(null=True)
    contact=models.CharField(max_length=250,null=True)
    caddress=models.IntegerField(null=True)

class Address(models.Model):
    receiver=models.CharField(max_length=20)#收件人
    detaiarea=models.CharField(max_length=150)#详细地址
    postcode=models.IntegerField()#邮政编码
    phone=models.BigIntegerField()#联系电话
    auser=models.ForeignKey("Userinfo")

