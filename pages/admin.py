from django.contrib import admin
from .models import Team
from django.utils.html import format_html
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50p" style="border_radius:100px"/>'.format(object.photo.url))


    thumbnail.short_description='photo'
    list_display=('id','thumbnail','first_name', 'Designation','created_date')
    list_display_links=('id','first_name', 'Designation','created_date')
    search_fields =('first_name',)
    list_filter=('Designation',)

admin.site.register(Team,TeamAdmin)