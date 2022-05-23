from django.contrib import admin
from .models import Db


@admin.register(Db)
class DbAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'pin', 'erp', 'pin_bank', 'image', 'image1', 'image2', 'created')
    search_fields = ('name', 'pin', 'pin_bank')
