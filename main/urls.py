from django.urls import path
from .views import *
from .models import *

urlpatterns =[
    path('profile/', user_profile, name='profile'),# Профиль пользователя
    path('register/', user_register, name='register'),# Регистрация
    path('login/', user_login, name='login'),# Авторизация 
    path('logout/', user_logout, name='logout'),# Выход
    path('', anime_list_view, name='anime-list'),#Отслеживание маршрута на главную страницу
    path('anime/<slug:slug>/', anime_detail_view, name='anime'),#Отслеживание маршрута на детальную страницу аниме
    path('chat/', chat, name='chat'),# Отслеживание маршрута на страницу чата
    path('favorite/', favorite, name='favorite'),# Отслеживание маршрута на страницу понравившиеся
    path('downloaded/', downloaded, name='downloaded'),# Отслеживание маршута на страницу скачанные
]
