from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path('random/', consumers.mainConsumer),
]