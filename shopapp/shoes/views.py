# views.py
from django.shortcuts import render
from .models import Shoes, Slider
from .forms import ShoeFilterForm

def home(request):
    sliders = Slider.objects.all()
    context = {
        'sliders': sliders,
    }
    return render(request, 'home.html', context)

def shoes(request):
    form = ShoeFilterForm(request.GET)
    shoes_query = Shoes.objects.all()

    if form.is_valid():
        shoes_query = form.filter_shoes(shoes_query)
    context = {
        'form': form,
        'shoes': shoes_query,
    }
    return render(request, 'shoes.html', context)


def shoe_detail(request, shoe_id):
    shoe = Shoes.objects.get(pk=shoe_id)
    return render(request, 'shoes_details.html', {'shoe': shoe})