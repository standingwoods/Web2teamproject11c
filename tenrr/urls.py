from django.urls import path
from tenrr import views
from .views import like_post
from .views import my_profile, edit_profile
from .views import add_comment_to_post, post_detail  # Added

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
    path('buy_post/<int:post_id>/', views.buy_post, name='buy_post'),
    path('confirm_purchase/<int:post_id>/', views.confirm_purchase, name='confirm_purchase'),
    path('complete_sale_page/<int:purchase_id>/', views.complete_sale_page, name='complete_sale_page'),
    path('add_funds/', views.add_funds, name='add_funds'),
    path('confirm_complete_sale/<int:purchase_id>/', views.confirm_complete_sale, name='confirm_complete_sale'),
    path('view_sale_media/<int:purchase_id>/', views.view_sale_media, name='view_sale_media'),
    path('hide_purchase/<int:purchase_id>/', views.hide_purchase, name='hide_purchase'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('post/<int:post_id>/comment/', add_comment_to_post, name='add_comment_to_post'),  # Added
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Added
]
