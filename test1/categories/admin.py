from django.contrib import admin
from .models import  category
# Register your models here.

class categorieAdmin(admin.ModelAdmin):
    search_fields=('title',)
admin.site.register(category,categorieAdmin)



