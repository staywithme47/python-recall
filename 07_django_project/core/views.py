from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset
# Create your views here.

def index(request):
    assets = Asset.objects.all()
    context = {
        'username' : "Иван",
        'assets' : assets
    }


    return render(request, 'core/index.html', context)
