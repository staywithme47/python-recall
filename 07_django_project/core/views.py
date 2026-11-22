from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Asset
from .forms import AssetForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('index')
    else:
        form = AssetForm()
    assets = Asset.objects.all()
    context = {
        'username' : "Иван",
        'assets' : assets,
        'form' : form,
    }


    return render(request, 'core/index.html', context)
