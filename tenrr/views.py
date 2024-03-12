from django.shortcuts import render
from django.http import HttpResponse

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

def login(request):
    context_dict = {'boldmessage': 'login'}
    return render(request, 'tenrr/login.html', context=context_dict)

def signup(request):
    context_dict = {'boldmessage': 'signup'}
    return render(request, 'tenrr/signup.html', context=context_dict)

