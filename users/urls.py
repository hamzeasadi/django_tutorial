from django.urls import path
from . import views as v

urlpatterns = [
    path('registration/', v.registration, name='user-registration'),
    path('login/', v.UserLoginView.as_view(), name='user-login')
]