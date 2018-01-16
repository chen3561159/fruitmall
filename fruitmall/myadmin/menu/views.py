from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import MenuFrom
from models import Menumessage
# Create your views here.
def add(request):
    pdata=Menumessage.objects.all()
    if request.method=="POST":
        f=MenuFrom(request.POST)
        if f.is_valid():
            print f.cleaned_data
            Menumessage.objects.create(**f.cleaned_data)
            return HttpResponseRedirect("/admin/menulist/")
        else:
            print f.errors
            errmesage = {"errs": f.errors}
            return render(request,'admin/menu/add.html',errmesage)
    data={'pdata':pdata}
    return render(request,'admin/menu/add.html',data)

def edit(request,id):
    if request.method=="POST":
        f = MenuFrom(request.POST)
        if f.is_valid():
            Menumessage.objects.update(**f.cleaned_data)
            return HttpResponseRedirect("/admin/menulist/")
        else:
            errmesage={"errs":f.errors}
            return render(request,'admin/menu/edit.html',errmesage)
    return render(request,'admin/menu/edit.html')

def deleted(request,id):
    if id :
        obj=Menumessage.objects.get(pk=id)
        obj.delete()
        return  HttpResponseRedirect("/admin/menulist/")


def mlist(request):
    return  render(request,'admin/menu/list.html')
