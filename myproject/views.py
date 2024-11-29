from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
from.models import compare
from.models import Iphone
from.models import Iphonepro
from.models import phonepro
from.models import Features
from.models import myphone
from.models import my
from.models import pro
from.models import ok
from.models import mm
from.models import sari
from.models import aaa
from.models import bbb
from.models import ts
from.models import ddd
from.models import eee
from.models import ggg



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout



# Create your views here.

def home(request):
    data = Product.objects.all()
    data1 = compare.objects.all()
    return render(request,"home.html",{"data": data,"data1":data1})

def navbar(request):
    return render(request,"navbar.html")

def footer(request):
    return render(request,"footer.html")

def about(request):
    return render(request,"about.html")

def add_to_cart(request):
    pass

def payment(request):
    return render(request,"payment.html")

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")
    else:
        return render(request,'login.html')



def logout_user(request):
    logout(request)
    return redirect("home")


def iphone16(request):
    data7 = myphone.objects.all()
    data8 = my.objects.all()
    data9 = pro.objects.all()
    data10 = ok.objects.all()
    return render(request,"iphone16.html",{"data7": data7,"data8": data8,"data9": data9,"data10": data10})

def iphone16pro(request):
    data3 = Iphone.objects.all()
    data4 = Iphonepro.objects.all()
    data5 = phonepro.objects.all()
    data6 = Features.objects.all()
    return render(request,"iphone16pro.html",{"data3": data3,"data4": data4,"data5": data5,"data6": data6})

def register(request):
    return render(request,"register.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Registration Success you can login now... {username}!")
            return redirect('login')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def iphone15(request):
    data11 = mm.objects.all()
    data12 = sari.objects.all()
    data13 = aaa.objects.all()
    data14 = bbb.objects.all()
    return render(request,"iphone15.html",{"data11": data11,"data12": data12,"data13": data13,"data14": data14})

def iphone14(request):
    data15 = ts.objects.all()
    data16 = eee.objects.all()
    data17 = ddd.objects.all()
    data18 = ggg.objects.all()
    return render(request,'iphone14.html',{"data15": data15,"data16": data16,"data17": data17,"data18": data18})






