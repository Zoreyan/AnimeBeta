from django.db import models

# Наша таблица где будут айпи адреса
class Ip(models.Model):
    ip = models.CharField(max_length=100)

# Модель жанров
class Genres(models.Model):
    title = models.CharField(max_length=90, verbose_name='Жанры')# Заголовок

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.title

# Модель категорий
class Category(models.Model):
    title = models.CharField(max_length=90)# Заголовок

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# Модель годов
class Year(models.Model):
    years = models.CharField(max_length=4, verbose_name='Года')# Заголовок

    class Meta:
        verbose_name = 'Year'
        verbose_name_plural = 'Years'

    def __str__(self):
        return self.years

# Модель сезонов
class Seasons(models.Model):
    seasons = models.CharField(max_length=4)

    def __str__(self):
        return self.seasons

# Модель серий
class Series(models.Model):
    series = models.CharField(max_length=4)

    def __str__(self):
        return self.series


# Модель Аниме
class Anime(models.Model):
    title = models.CharField(max_length=90)# Заголовок
    slug = models.SlugField(max_length=200)# Ссылка
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE, default='1', null=True, blank=True)# Сезон
    serie = models.ForeignKey(Series, on_delete=models.CASCADE, default='1', null=True, blank=True)# Серия
    image = models.ImageField(upload_to='images/')# Изобанжение, постер
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)# Связь с моделью категорий
    views_count = models.ManyToManyField(Ip, related_name="post_views", blank=True)# Счетчик просмотров
    genre  = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True, verbose_name='Жанры')# Связь с моделью жанров
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, verbose_name='Года')# Связь с моделью годов
    favorite = models.BooleanField(default=False)# Нравится ли аниме
    video = models.FileField(upload_to='videos/')# Видео плеер
    created = models.DateTimeField(auto_now_add=True)# Дата добавления аниме на сайт

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'

    def total_views(self):
        return self.views_count.count()

    def __str__(self):
        return self.title

