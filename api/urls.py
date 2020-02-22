
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from genAuth.views import SSOLogin, CreateUser, VerifyUser, LoginStepTwo
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]