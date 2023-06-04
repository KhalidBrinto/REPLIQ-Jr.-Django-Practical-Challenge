from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Asset, Employee, AssetAssignment
from .serializer import AssetAssignmentSerializer, AssetSerializer, EmployeeSerializer
# Create your views here.

# API endpoint to get all employees via REST API
@api_view(['GET'])
def getEmployee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# API endpoint to get all assets via REST API
@api_view(['GET'])
def getAsset(request):
    assets = Asset.objects.all()
    serializer = AssetSerializer(assets, many=True)
    return Response(serializer.data)

# API endpoint to get all asset assignments via REST API
@api_view(['GET'])
def getAssetAssignment(request):
    assetAsmt = AssetAssignment.objects.all()
    serializer = AssetAssignmentSerializer(assetAsmt, many=True)
    return Response(serializer.data)
