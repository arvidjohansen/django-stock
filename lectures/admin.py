from django.contrib import admin
from lectures.models import Lecture

# Register your models here.

class LectureManager(admin.ModelAdmin):
    
    list_display = ['name', 'description']
    search_fields = ['name']


admin.site.register(Lecture, LectureManager)
