from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate

def profile_not_created(user):
    return not hasattr(user, 'userprofile')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_profile')  # Redirect to create_profile view after signup
        else:
            messages.error(request, 'There was an error with your signup. Please correct the errors below.')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if profile_not_created(user):
                    return redirect('create_profile')  # Redirect to create_profile view after signin if profile not created
                else:
                    return redirect('home')  # Redirect to home view after signin

            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'There was an error with your signin. Please correct the errors below.')
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  # Redirect to home view after creating the profile
        else:
            messages.error(request, 'There was an error with your profile creation. Please correct the errors below.')
    else:
        form = UserProfileForm()

    # Check if the profile is already created, and redirect to home if true
    if not profile_not_created(request.user):
        messages.warning(request, 'Profile has already been created.')
        return redirect('home')

    return render(request, 'create_profile.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or any other desired page
