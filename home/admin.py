from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
  list_display = ['name','email','tel','text']
  search_fields = ['name']

admin.site.register(ContactModel,ContactAdmin)
admin.site.register(VideoModel1)