from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/some_endpoint/', MyConsumer.as_asgi()),
]