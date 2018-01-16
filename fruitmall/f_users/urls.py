from django.conf.urls import  url
import  views
urlpatterns = [
    url(r'login/', views.login,name='login'),
    url(r'register/',views.register,name='register'),
    url(r'center/',views.center,name='center'),
    url(r'^site/',views.site,name='site'),
    url(r'^addsite/',views.addsite,name='addsite'),
    url(r'^setcursite/',views.setcursite,name='setcursite'),
    url(r'^getaddress/',views.getaddress,name='getaddress'),
    url(r'^logout/',views.logout,name='logout'),
]