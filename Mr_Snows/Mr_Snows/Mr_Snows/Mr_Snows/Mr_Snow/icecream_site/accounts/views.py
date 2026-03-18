from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UserProfile
from orders.models import Order
from products.models import Product
from django.contrib.admin.views.decorators import staff_member_required



# LOGIN
def login_view(request):

    next_url = request.GET.get("next") or request.POST.get("next")

    if next_url == "None":
        next_url = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            if next_url:
                return redirect(next_url)

            return redirect("/cart/")   # FIXED

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html", {"next": next_url})


# SIGNUP
from django.contrib.auth.models import User
def signup(request):

    next_url = request.GET.get("next") or request.POST.get("next")

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        username = request.POST.get("username")   # ADD THIS LINE
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

            if User.objects.filter(username=username).exists():            messages.error(request, "User already exists")
            return redirect("signup")

        user = User.objects.create_user(
        username=username,
         password=password1
        )

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        login(request, user)

        if next_url:
            return redirect(next_url)

        return redirect("/cart/")

    return render(request, "signup.html", {"next": next_url})


        
       

# LOGOUT
def logout_view(request):

    logout(request)

    return redirect("/")




@staff_member_required
def admin_dashboard(request):

    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    total_users = User.objects.count()

    total_sales = sum(order.total_price for order in Order.objects.all())

    recent_orders = Order.objects.all().order_by('-id')[:5]

    # Monthly Sales Chart Data
    sales_data = [1200, 1900, 3000, 2500, 3200, 4100]

    context = {
        'total_orders': total_orders,
        'total_products': total_products,
        'total_users': total_users,
        'total_sales': total_sales,
        'recent_orders': recent_orders,
        'sales_data': sales_data
    }

    return render(request, 'admin_dashboard.html', context)