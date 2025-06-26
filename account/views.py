from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import loginForm

from django.contrib.auth import authenticate, login 
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                print("User is authenticated and active")
            # Log the user in and redirect to the home page or dashboard
            login(request, user)
            return redirect('video_list')  # Replace 'home' with your home page URL name
        else:
            # If the credentials are incorrect, show an error message
            return render(request, 'login2.html', {'error': 'Invalid username or password'})
    
    # If the request is GET, render the login page
    return render(request, 'login2.html')


def logout(request):
    logout(request)
    return redirect('login2.html')
    

def index(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "User already exist")
            if User.objects.filter(email = email).exists():
                messages.error(request, "email already taken")
            else:
                user = User.objects.create(username = username, email = email, password = pass1, first_name = fname, last_name = lname, is_active = True)
                user.save()
                if user is not None:
                    auth.login(request,user)
                    return render(request, 'home.html')


        else:
            messages.error(request, "password mismatch")
    else:
        return render(request, 'register2.html')
                

    return render(request,'register2.html')