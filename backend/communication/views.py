from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ChatRoom, Message, Notification
from django.contrib.auth.decorators import login_required


#@login_required
def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = Message.objects.filter(chat_room=room).order_by('-timestamp')
    return render(request, 'communication/chat_room.html', {'room': room, 'messages': messages})


#@login_required
def send_message(request):
    if request.method == "POST":
        message_text = request.POST.get('message')
        room_id = request.POST.get('room_id')
        room = ChatRoom.objects.get(id=room_id)
        message = Message.objects.create(chat_room=room, sender=request.user, message=message_text)
        return redirect('communication:chat_room', room_id=room_id)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)
    

#@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'communication/notifications.html', {'notifications': user_notifications})
