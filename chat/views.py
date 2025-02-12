from django.shortcuts import render
from django.http import HttpResponse

def chat_view(request):
    return render(request, 'chat/chat.html')
