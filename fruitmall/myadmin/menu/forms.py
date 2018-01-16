# -*- coding:utf-8 -*-
from  django import  forms
from  models import Menumessage
class MenuFrom(forms.Form):
    name=forms.CharField(max_length=50,required=True,error_messages={'required':"内容必须填写",'max_length':'不能超过50字符'})
    ismenu=forms.BooleanField()
    isDelete = forms.BooleanField()
    rank=forms.IntegerField(required=False)
    pid=forms.ModelChoiceField(queryset=Menumessage.objects.all(),required=False,empty_label=None)