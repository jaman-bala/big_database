from django.contrib import admin

# Register your models here.
from .models import Apps_lalafo


@admin.register(Apps_lalafo)
class Apps_lalafoAdmin(admin.ModelAdmin):
    list_display = ('nik_name', 'link', 'phone')
    search_fields = ('nik_name', 'link', 'phone')
