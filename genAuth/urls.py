
from django.contrib import admin
from django.urls import path
from genAuth.views import SSOLogin, CreateUser, VerifyUser, LoginStepTwo

urlpatterns = [
    path('login/', SSOLogin.as_view()),
    path('register/', CreateUser.as_view()),
    path('verify/', VerifyUser.as_view()),
    path('token/', LoginStepTwo.as_view()),
]
