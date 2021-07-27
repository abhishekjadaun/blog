from django.contrib import admin

# Register your models here.
from .models import BlogModel

@admin.register(BlogModel) # if decorator not use admin.site.register(Blog,BlogModel)
class Blog(admin.ModelAdmin):
    list_display=['title','desc','publish_date']
