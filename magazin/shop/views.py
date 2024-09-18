from django.shortcuts import render
from .models import *

def home(request):
    services = Service.objects.all() 
    return render(request, 'home.html', {'services': services})  

def portfolio(request):
    portfolios = Portfolio.objects.prefetch_related('images').all()

    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolio.html', context)