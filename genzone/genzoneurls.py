from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^login',views.login,name='login'),
    url(r'^contact',views.contact,name='contact'),
    url(r'^saveenq',views.saveenq,name='saveenq'),
    url(r'^custreg',views.custreg,name='custreg'),
    url(r'^validateuser',views.validateuser,name='validateuser'),
    url(r'^adminlogin',views.adminlogin,name='adminlogin'),
    url(r'^validateadmin',views.validateadmin,name='validateadmin'),

]