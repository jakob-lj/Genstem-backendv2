
from django.contrib import admin
from django.urls import path
from genAuth.views import SSOLogin, CreateUser

urlpatterns = [
    path('login/', SSOLogin.as_view()),
    path('register/', CreateUser.as_view()),
]
