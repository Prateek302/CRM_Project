from django.contrib import admin
from . models import Enquiry, Customer, AdminLogin

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Customer)
admin.site.register(AdminLogin)
