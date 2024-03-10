from django.urls import path
from tenrr import views


app_name = 'tenrr'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]