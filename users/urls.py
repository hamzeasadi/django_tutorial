from django.urls import path
from . import views as v
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registration/', v.registration, name='user-registration'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    path('profile/', v.profile, name='user-profile')
]