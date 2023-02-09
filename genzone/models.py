from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    message=models.CharField(max_length=500)

class Customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    age=models.IntegerField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(primary_key=True)
    password=models.CharField(max_length=20)
    regdate=models.CharField(max_length=20)

class AdminLogin(models.Model):
    adminid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
