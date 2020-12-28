from django.urls import path

from apps.views import index, dashboard, logout, login_redirect, kite_login,position,order_place

urlpatterns = [
    path('', index, name='index'),
    path('order_place/', order_place, name='order_place'),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout, name='logout'),
    path('login_redirect/', login_redirect, name="login_redirect"),
    path('kite_login/', kite_login, name="kite_login"),
    path('kite_position/', position, name="position"),
]
