from django.contrib import admin
from .models import Tool,Category,Employee,Designation,BorrowTool
# Register your models here.
admin.site.register(Tool)
admin.site.register(Category)
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(BorrowTool)