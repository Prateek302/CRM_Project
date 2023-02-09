from django.db import models

# Create your models here.
class Complain(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    contactno=models.CharField(max_length=50)
    emailaddress=models.EmailField()
    complaintext=models.CharField(max_length=1000)
    complaindate=models.CharField(max_length=20)

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    feedbacktext=models.CharField(max_length=100)
    feedbackdate=models.CharField(max_length=20)