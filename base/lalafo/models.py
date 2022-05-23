from django.db import models
from categories.models import Category, SubCategory, MinCategory


# Create your models here.

class Apps_lalafo(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT,
                                 verbose_name="Выберите область")
    subcategory = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.PROTECT,
                                    verbose_name="Выберите город")
    mincategory = models.ForeignKey(MinCategory, blank=True, null=True, on_delete=models.PROTECT,
                                    verbose_name="Выберите ")
    nik_name = models.CharField(max_length=255, verbose_name='Nikname')
    link = models.CharField(max_length=255, unique=True, verbose_name='Ссылка')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить данные "


        def __str__(self):
            return str(self.name)
