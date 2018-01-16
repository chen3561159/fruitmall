from django.conf.urls import include, url

from  categoty import views as cat

from  goods import  views as good

from  categoty import  views as categ

from  menu import views as menuview

urlpatterns = [
    url(r'^index/',good.index),
    url(r'^addgood/',good.addgood,name='addgood'),
    url(r'^goodlist/',good.list,name='goodlist'),
    url(r'^addtype/',categ.addcategory,name='addtype'),
    url(r'^typelist/',categ.categorylist,name='typelist'),
    url(r'^typedelete(\d+)/',categ.delete,name='typedelete'),
    url(r'^typedit(\d+)/',categ.edit,name='typedit'),
    url(r'^goodeidt(?P<id>\d+)',good.edit,name='goodeidt'),
    url(r'^goodelte(?P<id>\d+)',good.delete,name='goodelete'),
    url(r'^menulist',menuview.mlist,name='menulist'),
    url(r'^menuedit(?P<id>\d+)',menuview.edit,name='menuedit'),
    url(r'^menudelete(?P<id>\d+)',menuview.deleted,name='menudelete'),
    url(r'^menuadd',menuview.add,name='menuadd')
]