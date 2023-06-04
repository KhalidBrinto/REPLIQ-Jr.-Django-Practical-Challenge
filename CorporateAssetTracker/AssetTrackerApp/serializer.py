from rest_framework import serializers
from .models import Asset, Employee, AssetAssignment

# We need to create model serializers to render model data
# because the Response object cannot natively handle
# complex data types such as django model instances


# Serializer for Asset model
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

# Serializer for Employee model 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Serializer for AssetAssignment model 
class AssetAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAssignment
        fields = '__all__'


