from django.shortcuts import render
from .models import Shoes, Slider

def home(request):
    sliders = Slider.objects.filter(is_active=True)
    shoes = Shoes.objects.all()
    context = {
        'sliders': sliders,
        'shoes': shoes,
    }
    return render(request, 'home.html', context)
