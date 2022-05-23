# Generated by Django 3.2.9 on 2022-05-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20220520_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='db',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AddField(
            model_name='db',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='db',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создание'),
        ),
    ]
