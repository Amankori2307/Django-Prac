from django.urls import path
from .views import HTMLToPDFView
urlpatterns = [
    path("", HTMLToPDFView.as_view(), name="create_pdf")
]