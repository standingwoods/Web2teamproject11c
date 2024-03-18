from django.urls import path
from tenrr import views
from .views import like_post
from .views import my_profile, edit_profile

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
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
