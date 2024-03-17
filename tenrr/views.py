from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from tenrr.models import UserProfile
from tenrr.forms import UserProfileForm
from django.contrib import messages
from .forms import PostForm
from .models import Post, Category

# Signup view
def signup_view(request):
    context_dict = {'boldmessage': 'signup'}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        user_type = request.POST.get('user_type', 'Buyer')  # Default to 'Buyer' if not provided

        if password == confirm_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                user_profile = UserProfile(user=user, user_type=user_type)
                user_profile.save()
                # Optional: log the user in directly
                # login(request, user)
                return redirect('tenrr:login')  # This line seems correct. Ensure 'tenrr:login' is correctly defined in your urls.py
            except:
                messages.error(request, "Error creating user. Please try again.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'tenrr/signup.html', context=context_dict)

# Login view
def login_view(request):
    context_dict = {'boldmessage': 'login'}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed login function
            # Redirect to a success page or the 'next' parameter URL.
            next_url = request.GET.get('next', 'tenrr:index')  # 'tenrr:index' as default
            return redirect(next_url)
        else:
            messages.error(request, "Invalid login details.")
    else:
        # If there's a 'next' parameter, it means the user was redirected here
        # because they tried to access a login-required page.
        if 'next' in request.GET:
            messages.info(request, 'To make a post you must login.')

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
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', None)  
    categories = Category.objects.all()  
    posts = Post.objects.filter(content__icontains=query)


    if category_id:
        posts = posts.filter(category_id=category_id)

    context = {
        'posts': posts,
        'categories': categories,
        'selected_category_id': int(category_id) if category_id else None,
    }
    return render(request, 'tenrr/search.html', context)

def recommendations(request):
    return render(request, 'tenrr/recommendations.html', context=context_dict)

@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('tenrr:post') 
    else:
        form = PostForm() 
    
    return render(request, 'tenrr/post.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            user_profile.user_type = form.cleaned_data['user_type']
            user_profile.contact_info = form.cleaned_data['contact_info']
            user_profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('tenrr:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(initial={'username': user.username, 'email': user.email, 'user_type': user_profile.user_type, 'contact_info': user_profile.contact_info})
    return render(request, 'tenrr/edit_profile.html', {'form': form})
