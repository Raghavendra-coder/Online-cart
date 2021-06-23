from django.contrib import admin
from .models import Product, ProductCategory, SubCategory, Images, Contact, Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'counter')

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(SubCategory)
admin.site.register(Images)
admin.site.register(Contact)
admin.site.register(Cart, CartAdmin)



