from django.urls import re_path
# o re_path permite usar expressões regulares para definir as rotas

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer.as_asgi()),
] # Define a rota WebSocket para o chat, capturando o nome da sala como um parâmetro na URL