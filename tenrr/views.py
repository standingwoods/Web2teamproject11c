from django.shortcuts import render, redirect, get_object_or_404
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
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Like
from django.db.models import Exists, OuterRef
from django.db.models import Count, Q
from .models import Category

@login_required
def my_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_posts = Post.objects.filter(author=request.user).order_by('-created_date') 
    
    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_posts': user_posts,
    }
    return render(request, 'tenrr/my_profile.html', context)



# Signup view
def signup_view(request):
    context_dict = {'boldmessage': 'signup'}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        user_type = request.POST.get('user_type', 'Buyer')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                user_profile = UserProfile(user=user, user_type=user_type)
                user_profile.save()
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next', 'tenrr:index') 
            return redirect(next_url)
        else:
            messages.error(request, "Invalid login details.")
    else:
        if 'next' in request.GET:
            messages.info(request, 'To make a post you must login.')

    return render(request, 'tenrr/login.html', context=context_dict)

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('tenrr:index'))

def index(request):
    categories = Category.objects.all() 
    context_dict = {'boldmessage': 'happy', 'categories': categories}
    return render(request, 'tenrr/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'about'}
    return render(request, 'tenrr/about.html', context=context_dict)

def search(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    categories = Category.objects.all()

    posts = Post.objects.all()

    if query:
        posts = posts.filter(content__icontains=query)
    
    if category_id:
        posts = posts.filter(category_id=category_id)
    
    if min_price:
        posts = posts.filter(price__gte=min_price)
    
    if max_price:
        posts = posts.filter(price__lte=max_price)

    context = {
        'posts': posts,
        'categories': categories,
        'selected_category_id': int(category_id) if category_id else None,
    }
    return render(request, 'tenrr/search.html', context)

def search_view(request):
    user = request.user
    posts = Post.objects.all()

    category_id = request.GET.get('category', None)
    if category_id is not None:
        posts = posts.filter(category_id=category_id)

    if request.user.is_authenticated:
        likes_subquery = Like.objects.filter(user=request.user, post_id=OuterRef('pk'))
        posts = posts.annotate(user_has_liked=Exists(likes_subquery))
    else:
        posts = posts.annotate(user_has_liked=False)

    context = {'posts': posts}
    return render(request, 'search.html', context)


def recommendations(request):
    if request.user.is_authenticated:
        user = request.user
        liked_categories = Post.objects.filter(likes__user=user).values_list('category', flat=True).distinct()
        recommended_posts = Post.objects.filter(category__in=liked_categories).exclude(likes__user=user).annotate(likes_count=Count('likes')).order_by('-likes_count')[:10]
        return render(request, 'tenrr/recommendations.html', {'posts': recommended_posts})
    else:
        return render(request, 'tenrr/recommendations.html', {'login_prompt': True})



@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Thank you for making a post')
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
            return redirect('tenrr:my_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(initial={'username': user.username, 'email': user.email, 'user_type': user_profile.user_type, 'contact_info': user_profile.contact_info})
    return render(request, 'tenrr/edit_profile.html', {'form': form})

def ajax_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Please sign in to like a post'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@ajax_login_required
@require_POST
@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    liked = False  
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    
    if not created:
        like.delete()
    else:
        liked = True

    return JsonResponse({
        'likes_count': post.likes.count(),
        'liked': liked
    })

@login_required
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user) 
    post.delete()
    return redirect('tenrr:my_profile')