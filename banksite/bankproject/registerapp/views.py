from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages, auth
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('fillform')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "email taken")
            #     return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                print("User created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        # return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')