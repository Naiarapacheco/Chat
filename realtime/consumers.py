import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User
from .models import Message, Chat

class ChatConsumer(AsyncJsonWebsocketConsumer):

    # Entra no grupo de chat baseado no nome (chat_name)
    async def connect(self):
        self.chat_name = self.scope['url_route']['kwargs']['chat_name']
        self.chat_group_name = 'chat_%s' % self.chat_name

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    # Sai do grupo
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

     # Recebe mensagem e envia para o grupo
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        chat = data['chat']

        await self.save_message(username, chat, message)

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'chat': chat
            }
        )

    # Envia para o cliente que está conectado
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        chat = event['chat']

        await self.send(text_data=json.dumps({
                'message': message,
                'username': username,
                'chat': chat
        }))

    # Salvando a mensagem no banco de dados
    @sync_to_async
    def save_message(self, username, chat, message):
        user = User.objects.get(username=username)
        chat = Chat.objects.get(slug=chat)

        Message.objects.create(user=user, chat=chat, content=message)

