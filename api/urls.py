
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from genAuth.views import SSOLogin, CreateUser, VerifyUser, LoginStepTwo
from rest_framework_swagger.views import get_swagger_view
from api.views import EnvironmentView, StatusView

schema_view = get_swagger_view(title='Genstem API')

urlpatterns = [
    url(r'^docs/', schema_view),
    path('environment/', EnvironmentView.as_view()),
    path('connect/', StatusView.as_view()),
]