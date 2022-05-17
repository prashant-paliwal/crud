from django.contrib import admin
from .models import employees
# Register your models here.

class employeeAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']
admin.site.register(employees,employeeAdmin)