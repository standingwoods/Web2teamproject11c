from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    )
    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES, default='Buyer')
    contact_info = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

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
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='purchased_by', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    buyer_note = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} purchased {self.post.title}'

class PurchaseMedia(models.Model):
    purchase = models.ForeignKey('Purchase', related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='purchase_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Media for Purchase {self.purchase.id}'