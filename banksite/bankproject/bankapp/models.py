from django.db import models
from django.shortcuts import render
# Create your models here.
def login(request):

    return render(request,"loginapp/login.html")