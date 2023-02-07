from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def fillform(request):

    return render(request,'fillform.html')
def form(request):
    if request.method == 'POST':

        name = request.POST['Name']
        dob = request.POST['Date']
        age = request.POST['Age']
        gender = request.POST['Gender']
        number = request.POST['phone']
        email = request.POST['Email']
        address = request.POST['Address']
        district = request.POST['nFunction']

        user = authenticate(name=name,dob=dob,age=age,gender=gender,number=number,email=email,address=address,district=district)
        if name is not number:
           messages.success(request, "Application Created")
           return redirect('form')
        else:
            messages.info(request, "Fill all the fields")
            return redirect('form')
    return render(request,'form.html')