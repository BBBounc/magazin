from django.shortcuts import render
from .models import Service,Portfolio

def home(request):
    services = Service.objects.all() 
    return render(request, 'home.html', {'services': services})  
def portfolio(request):
    portfolio = Portfolio.objects.all() 
    return render(request, 'portfolio.html', {'portfolio': portfolio})  
