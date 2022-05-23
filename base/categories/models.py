from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Город, область "
        verbose_name_plural = "Кыргызстан "

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField("Название", max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Область, город"
        verbose_name_plural = "Город"

    def __str__(self):
        return self.name


class MinCategory(models.Model):
    name = models.CharField("Название", max_length=50)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Категория")


    class Meta:
        verbose_name = "Районы"
        verbose_name_plural = "Район"

    def __str__(self):
        return self.name
