from django.contrib import admin
from django.urls import path
from apps.views import index, dashboard, logout

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout, name='logout')
]
