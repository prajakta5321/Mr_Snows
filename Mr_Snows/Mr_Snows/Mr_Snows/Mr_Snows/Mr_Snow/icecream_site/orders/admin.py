from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'product',
        'quantity',
        'price',
        'total_amount',
        'phone',
        'ordered_date'
    )

    list_filter = (
        'ordered_date',
        'product'
    )

    search_fields = (
        'user__username',
        'phone',
        'product__name'
    )

    # FIX for Djongo delete bug
    def response_action(self, request, queryset):
        selected = request.POST.getlist('_selected_action')

        # remove None values
        selected = [i for i in selected if i != "None"]

        if not selected:
            return None

        queryset = queryset.filter(pk__in=selected)

        if request.POST.get('action') == 'delete_selected':
            queryset.delete()

        return None