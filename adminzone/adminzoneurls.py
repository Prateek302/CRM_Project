from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^product',views.product,name='product'),
    url(r'^customer',views.customer,name='customer'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^afeedback',views.afeedback,name='afeedback'),
    url(r'^acomplain',views.acomplain,name='acomplain'),
    url(r'^achangepassword',views.achangepassword,name='achangepassword'),
    url(r'^logout',views.logout,name='logout'),
]