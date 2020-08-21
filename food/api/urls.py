from django.urls import path
from food.api.view import registration_view

app_name = "food"

urlpatterns = [
    path('register', registration_view, name='register'),
]
