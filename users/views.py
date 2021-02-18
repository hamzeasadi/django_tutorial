from django.shortcuts import render, redirect
from . import forms as f
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User


def registration(request):
    if request.method == 'POST':
        form = f.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = f'Hello {username}, your account created successfully!!'
            messages.success(request, message)
            return redirect('blog-home')

    else:
        form = f.UserRegistrationForm()

    return render(request, 'users/registration.html', context={'form': form})


class UserLoginView(LoginView):

    class Meta:
        # model = User
        template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
