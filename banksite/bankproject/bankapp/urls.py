
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login.html',views.login,name="login"),
    path('register.html', views.register, name="register"),
    path('fillform.html', views.fillform, name="fillform"),
]