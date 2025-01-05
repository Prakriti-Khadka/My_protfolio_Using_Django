from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from home.models import Contact

def user_logout(request):
    auth_logout(request)
    return redirect('login')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            # Display form errors
            errors = form.errors.as_json()
            print(errors)  # For debugging, you can remove this later
            messages.error(request, 'Registration failed.')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
            # return redirect('contact')
        else:
            messages.error(request, 'This account is not registered.')
            return redirect('login')

    return render(request, 'login.html')

def index(request):
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(user=request.user, name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Successfully Submitted!")
    return render(request, 'contact.html')







