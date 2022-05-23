from django.db import models
from categories.models import Category, SubCategory, MinCategory


class Passport(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT, verbose_name="Выберите область")
    subcategory = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.PROTECT, verbose_name="Выберите город")
    mincategory = models.ForeignKey(MinCategory, blank=True, null=True, on_delete=models.PROTECT, verbose_name="Выберите ")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    name = models.CharField(max_length=255, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество")
    pin = models.CharField(max_length=255, unique=True, verbose_name="ПИН")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    erp = models.TextField(verbose_name="Фабула")
    image = models.FileField(upload_to='media', blank=True, verbose_name="Добавить фото")
    status = models.BooleanField(default=True)
    is_active = models.BooleanField("Активный", default=True)

    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить данные человека"
        ordering = ["-created"]

    def __str__(self):
        return str(self.name)
