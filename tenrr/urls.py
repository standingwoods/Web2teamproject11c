from django.urls import path
from tenrr import views

app_name = 'tenrr'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
