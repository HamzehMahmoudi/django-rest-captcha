from django.urls import path
from . import views


urlpatterns = [
    path('', views.RestCaptchaView.as_view(), name='dr_captcha'),
]
