from django.contrib import admin

from .models import Customer,Product,ShippingAddress,Order,OrderItem,service,Buy_parts,Review,FAQ

admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(service)
admin.site.register(Buy_parts)
admin.site.register(Review)
admin.site.register(FAQ)
