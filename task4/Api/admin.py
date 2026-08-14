from django.contrib import admin
from .models import recode

# Register your models here.
admin.site.register(recode)
class homeAdmin(admin.ModelAdmin):
     list_display=['name','email','message']
