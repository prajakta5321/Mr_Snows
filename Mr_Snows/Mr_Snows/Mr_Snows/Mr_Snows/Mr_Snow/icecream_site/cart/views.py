from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from products.models import Product
from orders.models import Order


# 🔹 Add product to cart
@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product_id=product.id,
        defaults={
            'product_name': product.name,
            'price': product.price,
            'quantity': 1
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/')


# 🔹 Buy now
@login_required
def buy_now(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    Cart.objects.create(
        user=request.user,
        product_id=product.id,
        product_name=product.name,
        price=product.price,
        quantity=1
    )

    return redirect('/cart/checkout/')


# 🔹 Cart page
@login_required
def cart_view(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# 🔹 Increase quantity
@login_required
def increase_quantity(request, cart_id):

    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('/cart/')


# 🔹 Decrease quantity
@login_required
def decrease_quantity(request, cart_id):

    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('/cart/')


# 🔹 Remove item from cart
@login_required
def remove_from_cart(request, cart_id):

    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)

    cart_item.delete()

    return redirect('/cart/')


# 🔹 Checkout
@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    if request.method == "POST":

        phone = request.POST.get('phone')
        address = request.POST.get('address')

        for item in cart_items:

            product = Product.objects.get(id=item.product_id)

            Order.objects.create(
                user=request.user,
                product=product,
                quantity=item.quantity,
                price=item.price,
                total_amount=item.price * item.quantity,
                phone=phone,
                address=address,
            )

        cart_items.delete()

        return redirect('order_success')

    total = sum(item.price * item.quantity for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

# 🔹 Order success page
@login_required
def order_success(request):
    return render(request, 'order_success.html')


# 🔹 My orders page
@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user).order_by('-id')

    return render(request, 'my_orders.html', {
        'orders': orders
    })

@login_required
def orders_page(request):

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'orders.html', {
        'orders': orders
    })