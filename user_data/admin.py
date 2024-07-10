from django.contrib import admin
from .models import User, Data
from django.conf import settings

class UserAdmin(admin.ModelAdmin):
    
    search_fields = ('name', 'role')
    list_display = ('name', 'role', 'email')
    
class DataAdmin(admin.ModelAdmin):
    
    search_fields = ('value', 'timestamp', 'description', 'cost', 'business_unit', 'other_data', 'valid_data')
    list_display = ('value', 'timestamp', 'description', 'cost', 'business_unit', 'other_data', 'valid_data')
    
admin.site.register(User, UserAdmin)
admin.site.register(Data, DataAdmin)
    
