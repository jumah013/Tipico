from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

#views
from.models import *
from .forms import CreateUserForm,CustomerForm,PasswordForm
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.core.mail import send_mail
from django.conf import settings

@unauthenticated_user
def registerpage(request):
    form=CreateUserForm()
    
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request,'Account was created for' + "" + username)
            return redirect('login')
    context={'form':form}
    return render(request,'accounts/register.html',context)

@unauthenticated_user
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('user')
        else:
            messages.info(request,'username OR password incorrect')
    
    context={}
    return render(request,'accounts/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        message_name=request.POST['message_name']
        message_email=request.POST['message_email']
        message=request.POST['message']

        send_mail(
            message_name,#subject111
            message,#message
            message_email,#from email
            ['jumabenjamin013@gmail.com'],# to email
        )
        return render(request,'accounts/contact.html',{'message_name':message_name})
    
    else:
   
        return render(request,'accounts/contact.html',{})
    
def about(request):
    return render(request,'accounts/about.html')

def payment(request):
    return render(request,'accounts/payment.html')

def payment1(request):
    return render(request,'accounts/payment1.html')


def payment2(request):
    return render(request,'accounts/payment2.html')


def payment3(request):
    return render(request,'accounts/payment3.html')

def vip(request):
    return render(request,'accounts/vip.html')
    
def packages(request):
    return render(request,'accounts/packages.html')
    
def freeodds(request):
    return render(request,'accounts/freeodds.html')

def success(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone']
        your_email = request.POST['your_email']
        your_address = request.POST['your_address']
        your_odd= request.POST['your_odd']
        your_date = request.POST['your_date']
        your_message = request.POST['your_message']


        booking = "Name: "+ your_name + " Phone: " +  your_phone + "Email:" +  your_email + "Address:" + your_address + "Odd:" + your_odd + "Date:" + your_date + "Message:" + your_message
        send_mail(
            'Booking Request',#subject111
            booking,#message
            your_email,#from email
            ['jumabenjamin013@gmail.com'],# to email
        )
        return render(request,'accounts/success.html',{
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule':your_odd,
            'your_date':your_date,
            'your_message':your_message

            })
    
    else:
        return render(request,'accounts/index.html')

def index(request):
    return render(request,'accounts/index.html')

@login_required(login_url='login')
def userpage(request):
    context={}
    return render(request,'accounts/user.html')

@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)

    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'accounts/accounts_settings.html',context)
