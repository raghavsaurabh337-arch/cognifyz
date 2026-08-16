from django.contrib import admin
from .models import recode,create

# Register your models here.
admin.site.register(recode)
class homeAdmin(admin.ModelAdmin):
     list_display=['name','email','message']

admin.site.register(create)
class createAdmin(admin.ModelAdmin):
     list_display=['name','email','password']   
