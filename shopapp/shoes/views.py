from django.shortcuts import render
from .models import Shoes, Slider

def home(request):
    sliders = Slider.objects.all()
    context = {
        'sliders': sliders,
    }
    return render(request, 'home.html', context)

def shoes(request):
    shoes = Shoes.objects.all()
    context={
        'shoes': shoes
    }
    return render(request,'shoes.html', context)

