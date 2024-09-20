from django.urls import path

from myapp.consumers import MySyncConsumer , MyAsyncConsumer,ChatAppSyncConsumer

websocket_urlpatterns = [
    path('ws/sc/',MySyncConsumer.as_asgi()),
    path('ws/ac/',MyAsyncConsumer.as_asgi()),
    path('ws/syc/<str:group_ka_name>/',ChatAppSyncConsumer.as_asgi()),
]