from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm

def home(request):
    return render(request, 'core/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
        messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')
