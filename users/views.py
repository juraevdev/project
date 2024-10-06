from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from .forms  import RegisterUserForm, UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def homepage(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {'form':form})
    else:
        form = UserLoginForm()
        return render(request, 'registration/login.html', {'form':form})
    
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.create(request.POST)
            return redirect('login')
    else:
        form = RegisterUserForm()
        return render(request, 'registration/signup.html', {'form':form})