from django.urls import path
from . import views

urlpatterns = [
    path('getemployees', views.getEmployee),
    path('getemployee/<id>', views.searchEmployee),
    path('getassets/', views.getAsset),
    path('getasset/<sr>', views.searchAsset),
    path('getassetassignments/', views.getAssetAssignment),
    path('getassetassignment/<id>', views.searchAssetAssignment),
]