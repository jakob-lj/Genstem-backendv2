
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from genAuth.views import SSOLogin, CreateUser, VerifyUser, LoginStepTwo
from vote.viewSets import EventSet
from rest_framework_swagger.views import get_swagger_view
from api.views import EnvironmentView, StatusView
from rest_framework import routers

schema_view = get_swagger_view(title='Genstem API')

router = routers.DefaultRouter()
router.register(r'events', EventSet)


urlpatterns = [
    url('^', include(router.urls)),
    url(r'^docs/', schema_view),
    path('environment/', EnvironmentView.as_view()),
    path('connect/', StatusView.as_view()),
]