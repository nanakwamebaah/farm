from ast import Return
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import FarmerSignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request,'farm/dash/includes/home_content.html', context)

def home(request):
    context = {}
    return render(request,'farm/home.html', context)    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            ''''
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User does not exist')
            '''
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else :
                messages.error(request, 'Username or password does not exist' )    
        context = {}
        return render(request,'farm/login.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = FarmerSignUpForm()

    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user_1 = form.save()
            user = form.cleaned_data.get('username')
            farmer = Farmer.objects.create(farmer=user_1)
            farmer.save()
            messages.success(request, 'Account was successfully created for' + user)
            return redirect('login')


    context = {'form':form}
    return render(request, 'farm/login_register.html', context)
    
@login_required(login_url='login')
def see_details(request):
    context={} 
    return render(request, 'farm/dash/includes/see_details.html', context)   
