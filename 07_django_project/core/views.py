from django.shortcuts import render, redirect, get_object_or_404
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

def asset_detail(request, asset_id: int):
    asset = get_object_or_404(Asset, id= asset_id)

    context = {
        'asset' : asset
    }
    return render(request, 'core/asset_detail.html', context)


def asset_update(request, asset_id: int):
    asset = get_object_or_404(Asset, id= asset_id)

    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_detail', asset_id = asset.id)
    else:
        form = AssetForm(instance=asset)

    context = {
        'form' : form,
        'asset' : asset,
    }
    return render(request, 'core/asset_form.html', context)