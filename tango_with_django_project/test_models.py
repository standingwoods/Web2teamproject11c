from django.test import TestCase
from django.contrib.auth.models import User
from tenrr.models import UserProfile, Post, Category

class UserProfileModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create(username='testuser', password='12345')
        user_profile = UserProfile.objects.create(user=user, user_type='Buyer')
        self.assertEqual(str(user_profile), 'testuser')

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
    
    def test_string_representation(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user, category=self.category)
        self.assertEqual(str(post), 'Test Post')
