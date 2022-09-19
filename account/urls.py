from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('account/register/sender/', views.SenderRegisterView.as_view()),
    path('account/register/buyer/', views.BuyerRegisterView.as_view()),
    path('', include('rest_framework.urls')),
]
