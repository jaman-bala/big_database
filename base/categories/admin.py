from django.contrib import admin
from categories.models import Category, SubCategory, MinCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "id")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "id")
    search_fields = ("name", "category__name")
    list_filter = ("category__name",)


@admin.register(MinCategory)
class MinCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "subcategory", "id")
    search_fields = ("name", "subcategory__name")
    list_filter = ("subcategory__name",)
