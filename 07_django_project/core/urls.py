
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name= 'index'),
               path('asset/<int:asset_id>/', views.asset_detail, name='asset_detail'),
               path('asset/<int:asset_id>/edit/', views.asset_update, name= 'asset_update'),
               path('asset/<int:asset_id>/delete/', views.asset_delete, name= 'asset_delete')
               ]

