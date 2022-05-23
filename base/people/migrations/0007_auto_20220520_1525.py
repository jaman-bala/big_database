# Generated by Django 3.2.9 on 2022-05-20 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('people', '0006_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mincategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AlterField(
            model_name='passport',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='mincategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.mincategory'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MinCategory',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]