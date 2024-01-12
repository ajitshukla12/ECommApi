# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("api_call", views.BookApiView.as_view(), name='your-model-list-create'),
    # Add more endpoints for other views
]
