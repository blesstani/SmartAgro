
from django.contrib import admin
from .models import Employee , Customer , Supplier, Transaction, Department,Task, Role, News,Document
# Register your models here.
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Transaction)
admin.site.register(Department)
admin.site.register(Task)
admin.site.register(Role)
admin.site.register(News)
admin.site.register(Document)