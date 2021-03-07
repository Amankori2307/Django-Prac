from django.urls import path
from . import views

urlpatterns = [
    path("create/",views.CreateXLSView.as_view(), name="create_xls")
]