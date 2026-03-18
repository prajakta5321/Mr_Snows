from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from accounts import views as account_views
from products import views as product_views
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return render(request, 'index.html')


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),

    path('login/', account_views.login_view, name='login'),
    path('signup/', account_views.signup, name='signup'),
    path('logout/', account_views.logout_view, name='logout'),

    # FRONTEND ADMIN
    path('admin-login/', product_views.admin_login, name='admin_login'),
    path('dashboard/', product_views.admin_dashboard, name='admin_dashboard'),
    path('add-product/', product_views.add_product, name='add_product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)