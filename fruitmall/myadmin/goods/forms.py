# -*- coding:utf-8 -*-
from  django import forms

class GoodForm(forms.Form):
    gname=forms.CharField(max_length=20,required=True,error_messages={'required':"商品名称必须填写",'max_length':"商品名不能超过20个字符"})
    intro=forms.CharField(max_length=200,required=False,error_messages={'max_length':"不可以超过200个字符"})
    stock = forms.IntegerField()
    unit=forms.CharField(max_length=20,error_messages={'max_length':"不能超过20个字符"})
    price=forms.DecimalField(max_digits=6,error_messages={'invalid':"请输入正确的价格"})
