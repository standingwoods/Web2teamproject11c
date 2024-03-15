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


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Endorsement(models.Model):
    user = models.ForeignKey(User, related_name='endorsements', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, related_name='endorsed_skills', on_delete=models.CASCADE)
    endorser = models.ForeignKey(User, related_name='given_endorsements', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'skill', 'endorser')

    def __str__(self):
        return f"{self.endorser} endorses {self.user} for {self.skill}"