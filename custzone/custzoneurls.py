from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^custhome',views.custhome,name='custhome'),
    url(r'^viewproducts',views.viewproducts,name='viewproducts'),
    url(r'^complain',views.complain,name='complain'),
    url(r'^feedback',views.feedback,name='feedback'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^raisecomplain',views.raisecomplain,name='raisecomplain'),
    url(r'^givefeedback',views.givefeedback,name='givefeedback'),
    url(r'^changepwd',views.changepwd,name='changepwd'),
]