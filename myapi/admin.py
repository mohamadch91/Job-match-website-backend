from django.contrib import admin
from .models import Job,Image


# Register your models here.
# admin.register() decorator

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'company', 'location',)

admin.site.register(Image)
