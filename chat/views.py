from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
# import random
# import string
# from django.db import transaction
# from django.shortcuts import render, redirect
# from haikunator import Haikunator
# from .models import Room
#
# def about(request):
#     return render(request, "chat/about.html")
#
# def new_room(request):
#     new_room = None
#     while not new_room:
#         with transaction.atomic():
#             haikunator = Haikunator()
#             label = haikunator.haikunate()
#             if Room.objects.filter(label=label).exists():
#                 continue
#             new_room = Room.objects.create(label=label)
#     return redirect(chat_room, label=label)
#
# def chat_room(request, label):
#     room, created = Room.objects.get_or_create(label=label)
#
#     messages = reversed(room.messages.order_by('-timestamp')[:50])
#
#     return render(request, "chat/room.html", {
#         'room': room,
#         'messages': messages,
#     })
