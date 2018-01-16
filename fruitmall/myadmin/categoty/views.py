from django.shortcuts import render
from  f_goods.models import Typeinfo
from  django.http import  HttpResponseRedirect
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def addcategory(request):
    if request.method=='POST':
        typemode=Typeinfo()
        tname=request.POST.get('tname',None)
        typemode.tname=tname
        typemode.save()
        if typemode.pk :
            return  HttpResponseRedirect('/admin/typelist/')

    return  render(request,'admin/categorys/addtype.html')

def categorylist(request):
    getpage=request.GET.get("page",1)
    data=Typeinfo.objects.all()
    paginator = Paginator(data, 10)
    page = request.GET.get('page')
    pagedata=paginator.page(getpage)
    content={'pagedata':pagedata}
    return  render(request,'admin/categorys/list.html',content)

def delete(request,id):
    if id :
        try:
            res = Typeinfo.objects.get(pk=id).delete()
            return HttpResponseRedirect('/admin/typelist/')
        except Exception:
            return HttpResponseRedirect('/admin/typelist/')



def edit(request,id):

    if request.method=="POST" and id :
            updict={}
            updict['tname']=request.POST.get('tname')
            res=Typeinfo.objects.filter(pk=id).update(**updict)
            if res :
                return  HttpResponseRedirect('/admin/typelist/')
    data=Typeinfo.objects.get(pk=id)
    content={"data":data}
    return render(request,'admin/categorys/edit.html',content)
