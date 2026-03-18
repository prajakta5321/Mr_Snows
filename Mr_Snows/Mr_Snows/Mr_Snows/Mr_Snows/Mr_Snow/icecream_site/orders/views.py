from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Order
from cart.models import Cart


# OFFLINE ORDER (Direct product checkout)
def offline_checkout(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        quantity = int(request.POST.get('quantity', 1))

        Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            product=product,
            quantity=quantity,
            price=product.price,
            total_amount=product.price * quantity,
            phone=request.POST.get('phone'),
            order_type=request.POST.get('order_type'),
        )

        return redirect('success')

    return render(request, 'checkout.html', {'product': product})


# CART → ORDER PAGE
def orders_page(request):

    orders = Order.objects.filter(user=request.user).order_by('-ordered_date')

    return render(request, 'orders.html', {'orders': orders})