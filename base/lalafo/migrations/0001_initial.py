# Generated by Django 3.2.9 on 2022-05-22 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0004_remove_subcategory_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps_lalafo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik_name', models.CharField(max_length=255, verbose_name='Nikname')),
                ('link', models.CharField(max_length=255, unique=True, verbose_name='Ссылка')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.category', verbose_name='Выберите область')),
                ('mincategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.mincategory', verbose_name='Выберите ')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory', verbose_name='Выберите город')),
            ],
            options={
                'verbose_name': 'Добавить',
                'verbose_name_plural': 'Добавить данные ',
            },
        ),
    ]
