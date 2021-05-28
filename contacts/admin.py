from django.contrib import admin
from . models  import contacts 

# Register your models here.

class Contactadmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','car_title','created_date')
    list_display_link=('id','first_name','last_name')
    search_fields=('first_name','last_name','email','car_title')
    list_per_page =25

admin.site.register(contacts,Contactadmin)
