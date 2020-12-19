from django.contrib import admin
from django.urls import path
from apps.views import index, dashboard, logout, login_redirect

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout, name='logout'),
    path('login_redirect/',login_redirect,name="login_redirect")
]
