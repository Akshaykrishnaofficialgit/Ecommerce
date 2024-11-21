from django.contrib import admin

from cart.models import Cart,Order_details,Payment_table

admin.site.register(Cart)
admin.site.register(Order_details)
admin.site.register(Payment_table)
# Register your models here.
