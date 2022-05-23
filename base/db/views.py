from django.shortcuts import render
from .forms import DbForm
from .models import Db


def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = DbForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            informations = Db.objects.all()
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'informations': informations})

    else:
        form = DbForm()
        informations = Db.objects.all()
    return render(request, 'index.html', {'form': form, 'index': index, 'informations': informations})

