from django.urls import re_path
from . import consumers

# WebSocket URL patterns for the chat app.
# This tells Django Channels to route any WebSocket connection that matches
# the pattern ws/<chat_name>/ to the ChatConsumer.

websocket_urlpatterns = [
    re_path(
        r'ws/(?P<chat_name>\w+)/$',  # Matches URL like ws/sala1/
        consumers.ChatConsumer.as_asgi()  # Calls the asynchronous consumer
    ),
]
