from django.contrib import admin
from tenrr.models import UserProfile
from tenrr.models import Category, Post, Like, Purchase, PurchaseMedia

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Purchase)
admin.site.register(PurchaseMedia)

