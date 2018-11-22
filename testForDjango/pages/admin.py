from django.contrib import admin

# Register your models here.
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display=('title','permalink', 'update_date')
    ordering=('title',)
    search_fields=('title',)


admin.site.register(Page, PageAdmin)# registe the page class in models.py
