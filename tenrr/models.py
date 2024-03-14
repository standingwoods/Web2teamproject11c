from django.db import models
from django.contrib.auth.models import User

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
