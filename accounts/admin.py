from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
	# the field to display
	list_display = ('id', 'name', 'email', 'tel')

admin.site.register(Customer, CustomerAdmin)