from django.contrib import admin
from .models import Asset, Employee, AssetAssignment

# Registering models to populate them from admin panel and
# also performing CRUD operations on models.
# username: admin, password: djdjdj12345
admin.site.register(Asset)
admin.site.register(Employee)
admin.site.register(AssetAssignment)
