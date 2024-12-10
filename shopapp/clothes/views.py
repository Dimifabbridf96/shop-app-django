from django.shortcuts import render
from .models import Clothes
from .forms import ClothesFilterForm

def clothes(request):
    form = ClothesFilterForm(request.GET)
    clothes_query = Clothes.objects.all()

    if form.is_valid():
        clothes_query = form.filter_clothes(clothes_query)
    context = {
        'form': form,
        'clothes': clothes_query,
    }
    return render(request, 'clothes.html', context)

def article_detail(request, clothes_id):
    article = Clothes.objects.get(pk=clothes_id)
    return render(request, 'article_detail.html', {'article': article})

