from django.shortcuts import render, redirect,reverse
from . models import Enquiry, Customer, AdminLogin
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def registration(request):
    return render(request, 'registration.html')
def login(request):
    return render(request, 'login.html')
def contact(request):
    return render(request, 'contact.html')

def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    message=request.POST['message']
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,message=message)
    enq.save()
    return redirect('index')

def custreg(request):
    password=request.POST['password']
    msg=''
    if len(password)<8:
        msg=msg+'Password Should Be Minimum 8 Char'
        return render(request,'registration.html',{'msg':msg})
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    age=request.POST['age']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    regdate=date.today()
    cust=Customer(name=name,gender=gender,address=address,age=age,contactno=contactno,emailaddress=emailaddress,password=password,regdate=regdate)
    cust.save()
    return redirect('login')

def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    msg=''
    try:
        user=Customer.objects.get(emailaddress=userid,password=password)
        if user is not None:
            request.session['userid']=userid
            return redirect(reverse('custzone:custhome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'login.html',{'msg':msg})

def adminlogin(request):
    return render(request,'adminlogin.html')

def validateadmin(request):
    adminid=request.POST['adminid']
    password=request.POST['password']
    msg='Message:'
    try:
        admin=AdminLogin.objects.get(adminid=adminid,password=password)
        if admin is not None:
            request.session['adminid']=adminid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'adminlogin.html',{'msg':msg})