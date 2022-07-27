# Generated by Django 4.0.5 on 2022-06-27 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_anime_year_alter_genres_title_alter_year_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='genre',
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.genres', verbose_name='Жанры'),
        ),
    ]