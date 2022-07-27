import django_filters
from .models import *

class AnimeFilter(django_filters.FilterSet):
    class Meta:
        model = Anime
        fields = ['genre', 'year']