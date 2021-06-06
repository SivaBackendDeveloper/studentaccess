from django.contrib import admin
from student.models import student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','mail','mobilenumber']

admin.site.register(student,StudentAdmin)