from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('send-message/', views.send_message, name='send_message'),
    path('notifications/', views.notifications, name='notifications'),
]
