# Generated by Django 3.2.9 on 2022-05-17 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_auto_20220517_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='db',
            options={'ordering': ['-created'], 'verbose_name': 'Добавить', 'verbose_name_plural': 'Добавить данные для Банка'},
        ),
    ]