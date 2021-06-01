from django.contrib import admin
from django.urls import path
# from .views  import Index,signup,Login
from .views import Home
from .views.signup import Signup
from .views.login import Login

urlpatterns = [
    path('',Home.as_view(),name='homepage'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login')
]
