from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tenrr.models import UserProfile
from django.contrib import messages

class MyProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user_profile = UserProfile.objects.create(user=self.user, user_type='Buyer')
        self.client.login(username='testuser', password='12345')
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/tenrr/my_profile/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('tenrr:my_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tenrr/my_profile.html')


    def test_view_handles_post_request(self):
        response = self.client.post(reverse('tenrr:my_profile'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'user_type': 'Buyer',
            'contact_info': 'Some contact info',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tenrr:my_profile'))
        self.assertContains(response, 'Profile updated successfully', status_code=302)
