from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Signup view
def signup_view(request):
    context_dict = {'boldmessage': 'signup'}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                # Optional: log the user in directly
                # login(request, user)
                return redirect('tenrr:login')
            except:
                messages.error(request, "Error creating user. Please try again.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'tenrr/signup.html', context=context_dict)

# Login view
def login_view(request):
    context_dict = {'boldmessage': 'login'}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed login function
            # Redirect to a success page.
            return redirect('index')  # Make sure you have an 'index' view or change this to the appropriate redirect
        else:
            # Return an 'invalid login' error message.
            pass
    # If GET request or other conditions, render your login form template
    return render(request, 'tenrr/login.html', context=context_dict)



@login_required
def logout_view(request):
    logout(request)
    # Redirect to the homepage or another appropriate page after logging out
    return redirect(reverse('tenrr:index'))

def index(request):
    context_dict = {'boldmessage': 'happy'}
    return render(request, 'tenrr/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'about'}
    return render(request, 'tenrr/about.html', context=context_dict)

def search(request):
    return render(request, 'tenrr/search.html', context=context_dict)

def recommendations(request):
    return render(request, 'tenrr/recommendations.html', context=context_dict)


