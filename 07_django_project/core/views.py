from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Asset
from .forms import AssetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import AssetForm, RegisterForm


@login_required
def index(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.owner = request.user
            asset.save()
            return redirect('index')
    else:
        form = AssetForm()
    assets = Asset.objects.filter(owner=request.user)
    context = {
        'username' : "Иван",
        'assets' : assets,
        'form' : form,
    }


    return render(request, 'core/index.html', context)


@login_required
def asset_detail(request, asset_id: int):
    asset = get_object_or_404(Asset, id= asset_id)

    context = {
        'asset' : asset
    }
    return render(request, 'core/asset_detail.html', context)


@login_required
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


@login_required
def asset_delete(request, asset_id:int):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        asset.delete()
        return redirect('index')

    return redirect('asset_detail', asset_id =asset.id)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form' : form })
