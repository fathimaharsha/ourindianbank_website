from django.urls import path
from . import views

urlpatterns = [
    path('fillform',views.fillform,name="fillform"),
    path('form',views.form,name="form"),
]