# Generated by Django 4.0.5 on 2022-06-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasons',
            name='seasons',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='series',
            name='series',
            field=models.CharField(max_length=4),
        ),
    ]
