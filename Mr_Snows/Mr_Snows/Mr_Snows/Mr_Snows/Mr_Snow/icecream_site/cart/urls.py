from django.urls import path
from . import views

urlpatterns = [

    path('', views.cart_view, name='cart'),

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('buy/<int:product_id>/', views.buy_now, name='buy_now'),

    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.my_orders, name='orders'),
    path('order-success/', views.order_success, name='order_success'),
    path('remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),

    path('decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    
]