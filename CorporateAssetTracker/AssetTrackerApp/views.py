from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Asset, Employee, AssetAssignment
from .serializer import AssetAssignmentSerializer, AssetSerializer, EmployeeSerializer
# Create your views here.

# API endpoint to get all employees via REST API
# example: /api/getemployees
@api_view(['GET'])
def getEmployee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# API endpoint to get employee by ID via REST API
# example: /api/getemployee/E03
@api_view(['GET'])
def searchEmployee(request, id):
    employee = Employee.objects.get(pk=id)
    print(employee)
    serializer = EmployeeSerializer(employee)
    print(serializer)
    return Response(serializer.data)

# API endpoint to get all assets via REST API
# example: /api/getassets
@api_view(['GET'])
def getAsset(request):
    assets = Asset.objects.all()
    serializer = AssetSerializer(assets, many=True)
    return Response(serializer.data)

# API endpoint to get Asset by serial via REST API
# example: /api/getasset/P02
@api_view(['GET'])
def searchAsset(request, sr):
    asset = Asset.objects.get(asset_serial=sr)
    serializer = AssetSerializer(asset)
    print(serializer)
    return Response(serializer.data)

# API endpoint to get all asset assignments via REST API
# example: /api/getassetassignments
@api_view(['GET'])
def getAssetAssignment(request):
    assetAsmt = AssetAssignment.objects.all()
    serializer = AssetAssignmentSerializer(assetAsmt, many=True)
    return Response(serializer.data)

# API endpoint to search asset assignment via REST API
# example: /api/getassetassignment/1
@api_view(['GET'])
def searchAssetAssignment(request, id):
    assetAsmt = AssetAssignment.objects.get(pk = id)
    serializer = AssetAssignmentSerializer(assetAsmt)
    return Response(serializer.data)
