from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .filter import AnimeFilter
from django.core.paginator import Paginator

def get_client_ip(request):
    x_forvarded_for = request.META.get('HTTP_X_FORVARDED_FOR')
    if x_forvarded_for:
        ip = x_forvarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Hentai List
def anime_list_view(request):
    category = Category.objects.all()
    genre = Genres.objects.all()
    anime = Anime.objects.all()
    paginator = Paginator(anime, 3)
    page = request.GET.get('page')

    animes = paginator.get_page(page)


    search_input = request.GET.get('q') or ''

    myFilter = AnimeFilter(request.GET, queryset=anime)
    if search_input:
        anime = Anime.objects.filter(title__icontains=search_input)
    
    elif myFilter:
        anime = myFilter.qs
    else:
        anime = Anime.objects.all()



    context = {
        'page': page,
        'animess': animes,
        'animes': anime,
        'myFilter': myFilter,
    }
    return render(request, 'main/anime_list.html', context)

# Hentai Detail
def anime_detail_view(request, slug):
    animes = Anime.objects.all()
    anime = Anime.objects.get(slug=slug)
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        anime.views_count.add(Ip.objects.get(ip=ip))

    else:
        Ip.objects.create(ip=ip)
        anime.views_count.add(Ip.objects.get(ip=ip))


    context = {
        'animes': animes,
        'anime': anime,
    }
    return render(request, 'main/anime_detail.html', context)

# User Sign up
def user_register(request):
    if request.user.is_authenticated:
        return redirect('anime-list')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)
# User Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('anime-list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('anime-list')
        context = {}
        return render(request, 'main/login.html', context)

# User Logout
def user_logout(request):
    logout(request)
    return redirect('anime-list')

# Chat
@login_required(login_url='login')
def chat(request):
    context = {}
    return render(request, 'main/chat.html', context)

# Favorite
@login_required(login_url='login')
def favorite(request):
    favorite = Anime.objects.filter(favorite=True)
    

    context = {
        'favorites': favorite
    }
    return render(request, 'main/favorite.html', context)

# Downloaded
@login_required(login_url='login')
def downloaded(request):
    context = {}
    return render(request, 'main/downloaded.html', context)

# Watched
@login_required(login_url='login')
def history(request):
    context = {}
    return render(request, 'main/history.html', context)

def user_profile(request):
    context = {}
    return render(request, 'main/profile.html', context)