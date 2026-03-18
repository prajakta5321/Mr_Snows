from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from orders.models import Order


# ---------------- PRODUCTS PAGE ----------------
def product_list(request):

    products = Product.objects.all()

    return render(request, "products.html", {"products": products})


# ---------------- CONTACT ----------------
def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print("CONTACT:", name, email, message)

        return redirect("contact")

    return render(request, "contact.html")


# ---------------- CHECKOUT ----------------
def checkout(request):

    if request.method == "POST":

        customer_name = request.POST.get("customer_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        total_amount = request.POST.get("total_amount")

        Order.objects.create(
            customer_name=customer_name,
            phone=phone,
            address=address,
            total_amount=total_amount
        )

        return redirect("home")

    return render(request, "checkout.html")


# ---------------- ADD TO CART ----------------
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session["cart"] = cart

    return redirect("checkout")


# ---------------- ADMIN LOGIN ----------------

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['admin'] = True
            return redirect('admin_dashboard')

    return render(request, "admin_login.html")


# ---------------- ADMIN DASHBOARD ----------------

def admin_dashboard(request):

    if not request.session.get('admin'):
        return redirect('admin_login')

    products = Product.objects.all()

    return render(request, "admin_dashboard.html", {"products": products})


# ---------------- ADD PRODUCT ----------------

def add_product(request):

    if not request.session.get('admin'):
        return redirect('admin_login')

    if request.method == "POST":

        name = request.POST.get("name")
        type = request.POST.get("type")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        Product.objects.create(
            name=name,
            type=type,
            price=price,
            image=image
        )

        return redirect('admin_dashboard')

    return render(request, "add_product.html")


# ---------------- DELETE PRODUCT ----------------

def delete_product(request, id):

    product = get_object_or_404(Product, id=id)

    product.delete()

    return redirect('admin_dashboard')