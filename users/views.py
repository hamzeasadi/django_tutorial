from django.shortcuts import render, redirect
from . import forms as f
from django.contrib import messages
# from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == 'POST':
        form = f.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = f'Hello {username}, your account created successfully!!'
            messages.success(request, message)
            return redirect('user-login')

    else:
        form = f.UserRegistrationForm()

    return render(request, 'users/registration.html', context={'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
