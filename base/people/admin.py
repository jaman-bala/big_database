from django.contrib import admin
from .models import Passport


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'pin', 'image', 'created')
    search_fields = ('name', 'pin', 'address')



