# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from  models import Userinfo,Address
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import  hashlib
# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd")
        remember = request.POST.get("remember")
        if remember=='1':
            request.session['lgname']=uname
        else:

             if request.session.has_key('lgname'):
                 del request.session['lgname']


        data = Userinfo.objects.filter(uname=uname)

        if not any(data):
            err={'uerr':"用户名不存在"}
            return render(request, 'home/f_users/login.html',err)

        m5=hashlib.md5()
        m5.update(pwd)
        mdpwd=m5.hexdigest()

        if mdpwd!=data[0].pwd:
            err = {'perr': "密码错误"}
            return render(request, 'home/f_users/login.html',err)
        else:
            request.session['id']=data[0].id
            request.session['uname']=data[0].uname
            red=HttpResponseRedirect("/user/center/")
            red.set_cookie('uname',uname)
            return  red

    return render(request,'home/f_users/login.html')

def logout(request):
    del  request.session['id']
    return  HttpResponseRedirect("/user/login/")

def register(request):
    if request.method=='POST':
        m=Userinfo()
        cpwd=request.POST.get("cpwd")
        m.uname=request.POST.get("uname")
        m.pwd=request.POST.get('pwd')
        if cpwd!=m.pwd:
            err={"cpwd":'两次密码不一致'}
            return render(request,'home/f_users/register.html',err)
        m5=hashlib.md5()
        m5.update(m.pwd)
        m.pwd =m5.hexdigest()
        m.save()
        if m.pk :
            return  render(request,'home/f_users/login.html')

    return render(request, 'home/f_users/register.html')

def center(request):
    uid=request.session.get('id')
    data=Userinfo.objects.get(id=uid)
    content={'udata':data}
    return render(request,'home/f_users/user_center_info.html',content)


def site(request):
    uid = request.session.get('id')
    udata=Userinfo.objects.get(id=uid)
    senduid = request.POST.get('senduid')
    senduid=int(senduid) if senduid else senduid
    if request.method=='POST' and senduid==uid:
        aid=request.POST.get('aid').strip()
        aid=int(aid)
        address=Address.objects.get(id=aid)
        address.receiver=request.POST.get('receiver').strip()
        address.detaiarea=request.POST.get('detaiarea').strip()
        address.postcode=request.POST.get('postcode').strip()
        address.phone=request.POST.get('phone').strip()
        address.auser=udata
        address.save()
    dress = udata.address_set.all()
    content={'udata':udata,'dress':dress}
    return  render(request,'home/f_users/user_center_site.html',content)

def addsite(request):
    uid=request.session.get('id')
    udata = Userinfo.objects.get(id=uid)
    if request.method=='POST':
        address=Address()
        address.receiver=request.POST.get('receiver').strip()
        address.detaiarea=request.POST.get('detaiarea').strip()
        address.postcode=request.POST.get('postcode').strip()
        address.phone=request.POST.get('phone').strip()
        address.auser=udata
        address.save()
        if address.pk:
            return HttpResponseRedirect('/user/site/')
    content={'udata':udata}
    return render(request,'home/f_users/user_center_addsite .html',content)

@csrf_exempt
def setcursite(request):
    uid=request.POST.get('uid')
    addressid=request.POST.get('addressid')
    udata=Userinfo.objects.get(id=uid)
    udata.caddress=int(addressid)
    udata.save()
    if udata.pk:
        message=[{'res':'ok'}]
    else:
        message=[{'res':'ok'}]

    return JsonResponse(message, safe=False)

@csrf_exempt
def getaddress(request):
    uid = request.session.get('id')
    if uid:
        aid=request.POST.get('aid')
        adata=Address.objects.get(id=aid)
        list=[{'res':'ok'}]
        list.append({'receiver':adata.receiver,'detaiarea':adata.detaiarea,'postcode':adata.postcode,'phone':adata.phone})
    else:
        list=[{'res':'无权修改'}]
    return JsonResponse(list,safe=False)

