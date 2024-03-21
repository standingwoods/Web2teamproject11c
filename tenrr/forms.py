from django import forms
from django.contrib.auth.models import User
from tenrr.models import UserProfile, Comment  # Added Comment model import
from .models import Post
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Please enter your username.")
    email = forms.EmailField(max_length=254, help_text="Please enter your email.")
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, help_text="Are you a buyer or seller?")
    contact_info = forms.CharField(widget=forms.Textarea, required=False, help_text="Please enter your contact information.")

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'contact_info')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'price']
        error_messages = {
            'price': {
                'invalid': "Enter a valid number.",
            },
        }
   
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Ensure this value is greater than or equal to 0.')
        return price


class CommentForm(forms.ModelForm):  # Added CommentForm class
    class Meta:
        model = Comment
        fields = ['text']
