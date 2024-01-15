# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("api_call", views.BookApiView.as_view(), name='your-model-list-create'),
    path("api_call_qunatity", views.BookQunatity.as_view(),name='quantity'),
    # Add more endpoints for other views
]
