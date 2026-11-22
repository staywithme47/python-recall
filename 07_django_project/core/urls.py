
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name= 'index'),
               path('asset/<int:asset_id>/', views.asset_detail, name='asset_detail'),

               ]

