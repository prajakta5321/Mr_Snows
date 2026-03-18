from django.contrib import admin
from .models import Product, Order

admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = None

    list_display = (
        'id',
        'name',
        'flavour',
        'type',
        'price',
        'stock',
    )

    list_filter = ('type',)

    search_fields = ('name','flavour')


admin.site.register(Product, ProductAdmin)

# register orders in admin
admin.site.register(Order)