from django.shortcuts import render
from f_goods.models import Goodsinfo
from  f_goods.models import Typeinfo
from  forms import GoodForm
from django.http import  HttpResponseRedirect
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'admin/base_index.html')


def addgood(request):
    if request.method=="POST":
        f=GoodForm(request.POST)
        if f.is_valid():
            print f.cleaned_data
            f.cleaned_data['details'] = request.POST.get("details")
            model=Goodsinfo.objects.create(**f.cleaned_data)
            model.gtype=request.POST.getlist('gtype')
            model.save()
            return HttpResponseRedirect("/admin/goodlist/")
        else:
            errs={"errorlist":f.errors}
            print errs
            return render(request, 'admin/goods/addgood.html',errs)
    typedata=Typeinfo.objects.all()

    typedata={'typedata':typedata}
    return render(request,'admin/goods/addgood.html',typedata)

def list(request):
    getpage=request.GET.get("page",1)
    data=Goodsinfo.objects.all()
    print data[6].gtype.all()
    paginator = Paginator(data, 10)
    page = request.GET.get('page')
    pagedata=paginator.page(getpage)
    content={'pagedata':pagedata}
    return  render(request,'admin/goods/list.html',content)

def edit(request,id):
    data=Goodsinfo.objects.get(pk=id)
    if request.method=="POST":
        f=GoodForm(request.POST)
        if f.is_valid():
            f.cleaned_data['details']=request.POST.get("details")
            model=Goodsinfo.objects.filter(pk=id).update(**f.cleaned_data)
            data.gtype=request.POST.getlist('gtype')
            print request.POST.getlist('gtype')
            return HttpResponseRedirect("/admin/goodlist/")
        else:
            errs = {"errorlist": f.errors}
            return render(request, 'admin/goods/edit.html', errs)
    typedata = Typeinfo.objects.all()
    bltype=data.gtype.all()
    belong=[ i.id for i in bltype]
    content = {'data': data,'typedata':typedata,'belong':belong}
    return render(request, 'admin/goods/edit.html', content)


def delete(request,id):
    if id :
        try:
            gdata = Goodsinfo.objects.get(pk=id)
            gdata.gtype.clear()
            gdata.delete()
            return HttpResponseRedirect('/admin/goodlist/')
        except Exception:
            return HttpResponseRedirect('/admin/goodlist/')
