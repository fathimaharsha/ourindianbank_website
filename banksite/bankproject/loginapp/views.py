from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib import messages, auth
# from django.core.checks import messages
# from django.contrib.auth.models import User
# # Create your views here.
# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#           auth.login(request,user)
#           return redirect('fillform')
#         else:
#             messages.info(request,"Invalid credentials")
#             return redirect('login')
#     return render(request,'login.html')