from django.contrib import admin
from .models import Result, Result_Sheet

class ResultAdmin(admin.ModelAdmin):
    list_display = ('session', 'semester', 'level', 'tcr', 'tce', 'gpa', 'cgpa', 'remark', 'details')
    

class Result_SheetAdmin(admin.ModelAdmin):
    list_display = ('sn', 'course_code', 'course_title', 'category', 'grade')
    
admin.site.register(Result, ResultAdmin)
admin.site.register(Result_Sheet, Result_SheetAdmin)