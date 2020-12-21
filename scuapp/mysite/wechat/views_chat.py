# chat/views.py
from django.shortcuts import render
from django.shortcuts import HttpResponse,render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json




def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })





