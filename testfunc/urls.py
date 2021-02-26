from django.urls import path
from . import views

urlpatterns = [
    path("auth/", views.AuthTest.as_view())
]