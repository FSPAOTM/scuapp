# mysite/asgi.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from mysite import routing

# import scuapp.mysite.wechat.routing


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})