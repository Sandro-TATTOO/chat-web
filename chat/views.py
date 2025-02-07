from django.shortcuts import render
from django.http import HttpResponse

def chat_view(request):
    return HttpResponse("Bem-vindo ao chat!")
