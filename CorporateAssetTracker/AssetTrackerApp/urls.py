from django.urls import path
from . import views

urlpatterns = [
    path('getemployees', views.getEmployee),
    path('getassets/', views.getAsset),
    path('getassetassignments/', views.getAssetAssignment),
]