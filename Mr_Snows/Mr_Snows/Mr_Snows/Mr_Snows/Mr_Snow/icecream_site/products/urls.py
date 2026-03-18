from django.urls import path
from .views import product_list, contact, admin_login, checkout
from . import views

urlpatterns = [

    # PRODUCT LIST PAGE
    path('', product_list, name='products'),

    # CONTACT
    path('contact/', contact, name='contact'),

    # ADMIN LOGIN
    path('admin/', admin_login, name='admin'),

    # CHECKOUT
    path('checkout/', checkout, name='checkout'),


    path('dashboard/',views.admin_dashboard,name="dashboard"),
path('add-product/',views.add_product,name="add_product"),
path('delete-product/<int:id>/',views.delete_product,name="delete_product"),

    
]