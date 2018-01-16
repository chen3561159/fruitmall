from django.db import models
from  tinymce.models import  HTMLField
from f_users.models import Userinfo

class Typeinfo(models.Model):
    tname=models.CharField(max_length=50)
    goods=models.ManyToManyField('Goodsinfo')


class Goodsinfo(models.Model):
    gname=models.CharField(max_length=20)
    intro=models.CharField(max_length=200,null=True)
    unit=models.CharField(max_length=20,null=True)
    stock=models.IntegerField(default=0)
    isdelete=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    details=HTMLField(null=True)
    click=models.IntegerField(default=0)
    recom=models.IntegerField(default=0)
    salenum=models.IntegerField(default=0)
    gtype=models.ManyToManyField('Typeinfo')

class Goodpic(models.Model):
    imgsrc=models.CharField(max_length=100)
    gid=models.ForeignKey('Goodsinfo')


class Shopcar(models.Model):
    gid=models.ForeignKey("Goodsinfo")
    uid=models.ForeignKey('f_users.Userinfo')

