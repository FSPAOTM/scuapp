# chat/routing.py
from django.urls import re_path

from wechat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/chatgroup/(?P<group_name>\w+)/$', consumers.ChatGroupConsumer.as_asgi()),
]