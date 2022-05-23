from django.shortcuts import render
from .models import Passport
from categories.models import Category, SubCategory, MinCategory
from .forms import PassportForm


def main(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PassportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            passports = Passport.objects.all()
            categories = Category.objects.all()
            subcategories = SubCategory.objects.all()
            mincategories = MinCategory.objects.all()
            return render(request, 'main.html',
                          {'form': form, 'img_obj': img_obj,
                           'passports': passports, 'categories': categories,
                           'subcategories': subcategories, 'mincategories': mincategories})

    else:
        form = PassportForm()
        passports = Passport.objects.all()
    return render(request, 'main.html', {'form': form, 'passports': passports})


