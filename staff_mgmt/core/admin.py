from django.contrib import admin
from .models import Department, Staff, Attendance

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'position', 'hire_date')
    list_filter = ('department', 'position')
    search_fields = ('name', 'email')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('staff__name',)
