from django import forms
from django.contrib.auth.models import User
from tenrr.models import UserProfile
from tenrr.models import UserProfile, Skill, Endorsement 

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Please enter your username.")
    email = forms.EmailField(max_length=254, help_text="Please enter your email.")
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, help_text="Are you a buyer or seller?")
    contact_info = forms.CharField(widget=forms.Textarea, required=False, help_text="Please enter your contact information.")

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'contact_info')

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

class EndorsementForm(forms.ModelForm):
    class Meta:
        model = Endorsement
        fields = ['skill', 'endorser']