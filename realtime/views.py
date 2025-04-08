from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Chat, Message

@login_required
def chats(request):
    chats = Chat.objects.all()

    return render(request, 'chats/chats.html', {'chats': chats})

@login_required
def chat(request, slug):
    chat = Chat.objects.get(slug=slug)
    mensage = Message.objects.filter(chat=chat)[0:25]
    
    return render(request, 'chats/chat.html', {'chat': chat, 'mensage': mensage})