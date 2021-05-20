from django.contrib import admin
from django.utils.html import format_html

from .models import Car
# Register your models here.


class Carmodel(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50p" style="border_radius:100px"/>'.format(object.car_photo1.url))
    thumbnail.short_description='photo'
    list_display=('id','car_title','thumbnail','state','color','model','year','body_style','fuel_type','is_features')
    list_display_links=('id','car_title','thumbnail')
    search_fields=('id','car_title','model','body_style','fuel_type')
    list_filter=('id','car_title','fuel_type')
    list_editable=('is_features',)
admin.site.register(Car,Carmodel)