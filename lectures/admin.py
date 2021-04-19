from django.contrib import admin
from lectures.models import Lecture, Inquiry

# Register your models here.

class LectureManager(admin.ModelAdmin):
    
    list_display = ['name', 'description','active']
    search_fields = ['name']


admin.site.register(Lecture, LectureManager)


class InquiryManager(admin.ModelAdmin):
    
    list_display = ['name', 'email','description']
    search_fields = ['name']


admin.site.register(Inquiry, InquiryManager)
