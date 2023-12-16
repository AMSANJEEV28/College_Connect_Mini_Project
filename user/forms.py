# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import UserProfile

CustomUser = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'college_name', 'university_name', 'registration_id', 'date_of_birth', 'gender', 'profile_picture', 'department', 'course']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'college_name': 'Enter your college name',
            'university_name': 'Enter your university name',
            'registration_id': 'Enter your registration ID',
            'date_of_birth': 'Select your date of birth',
            'gender': 'Select your gender',
            'profile_picture': 'Upload your profile picture',
            'department': 'Enter your department',
            'course': 'Enter your course',
        }

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
