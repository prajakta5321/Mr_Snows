from django.urls import path
from . import views
from .views import admin_dashboard


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

]