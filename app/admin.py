from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Contact,Product,Order
# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
