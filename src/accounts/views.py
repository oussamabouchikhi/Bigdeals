from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserForm, ProfileForm
# Create your views here.

def signup(request):
    # if user accessed with a post request
    if request.method == 'POST':
        # get all data from post request
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_date.get('username')
            password = form.cleaned_date.get('password')

            user = authenticate(username = username, password = password)
            login(request, user)
            # redirect user to products page after login
            return redirect('/products')
    else:
        # form will be empty
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
