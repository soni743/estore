from django.contrib import admin
from django.urls import path
from .views  import Index,signup,Login

urlpatterns = [
    path('', Index,name='homepage'),
    path('signup/',signup),
    path('login/',Login.as_view())
]
