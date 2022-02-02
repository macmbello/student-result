from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('fname', 'sname', 'department', 'reg_no', 'dob')
    
admin.site.register(Profile, ProfileAdmin)