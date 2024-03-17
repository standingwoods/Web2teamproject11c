from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    )
    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES, default='Buyer')
    contact_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Set the price in GBP.", default=0.00)

    def __str__(self):
        return self.title