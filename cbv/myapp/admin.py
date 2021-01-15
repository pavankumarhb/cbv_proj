from django.contrib import admin
from myapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    l=['number','name','marks','place']
admin.site.register(Student,StudentAdmin)
