from django.contrib import admin
from .models import *
# Админка аниме
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created', 'favorite']# Отображает значения указанные в списке
    prepopulated_fields = {'slug': ('title',)}# Вставляет значение title в поле ссылки slug
    list_editable = ['favorite']# Дает возможность менять значение
admin.site.register(Anime, AnimeAdmin)

# Вывод на страницу админки Год, Категории и Жанры
admin.site.register(Genres)
admin.site.register(Category)
admin.site.register(Year)
admin.site.register(Series)
admin.site.register(Seasons)