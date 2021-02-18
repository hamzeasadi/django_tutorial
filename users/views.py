from django.shortcuts import render, redirect
from . import forms as f
from django.contrib import messages


def registration(request):
    if request.method == 'post':
        form = f.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = f'Hello {username}, your account created successfully!!'
            messages.success(request, message)
            return redirect(request, 'blog-home')

    else:
        form = f.UserRegistrationForm()

    return render(request, 'users/registration.html', context={'form': form})
