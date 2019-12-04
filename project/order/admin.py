from django.contrib import admin

from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'delivered', 'paid', 'date', 'time']
admin.site.register(Order, OrderAdmin)