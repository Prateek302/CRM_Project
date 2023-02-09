from django.shortcuts import render

# Create your views here.
def adminhome(request):
    try:
        if request.session['adminid']:
            return render(request,'adminhome.html')
    except KeyError:
        return render(request,'adminlogin.html')

def product(request):
    try:
        if request.session['adminid']:
            return render(request,'product.html')
    except KeyError:
        return render(request,'adminlogin.html')

def customer(request):
    try:
        if request.session['adminid']:
            return render(request,'customer.html')
    except KeyError:
        return render(request,'adminlogin.html')

def enquiry(request):
    try:
        if request.session['adminid']:
            return render(request,'enquiry.html')
    except KeyError:
        return render(request,'adminlogin.html')

def afeedback(request):
    try:
        if request.session['adminid']:
            return render(request,'afeedback.html')
    except KeyError:
        return render(request,'adminlogin.html')

def acomplain(request):
    try:
        if request.session['adminid']:
            return render(request,'acomplain.html')
    except KeyError:
        return render(request,'adminlogin.html')

def achangepassword(request):
    try:
        if request.session['adminid']:
            return render(request,'achangepassword.html')
    except KeyError:
        return render(request,'adminlogin.html')

def logout(request):
    try:
        if request.session['adminid']:
            request.session['adminid']=None
            return render(request,'adminlogin.html')
    except KeyError:
        return render(request,'adminlogin.html')