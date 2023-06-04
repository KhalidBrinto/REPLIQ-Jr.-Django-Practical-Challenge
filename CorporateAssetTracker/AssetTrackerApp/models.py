from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

ASSET_CHOICES = (
    ("Desk", "Desk"),
    ("Laptop", "Laptop"),
    ("Phone", "Phone"),
    ("Tablet", "Tablet"),
    ("Printer", "Printer")
)

DEPARTMENTS = (
    ("Accounts", "Accounts"),
    ("IT", "IT"),
    ("Planning", "Planning"),
    ("Marketing", "Marketing"),
    ("Corporate", "Corporate"),
    ("HR", "HR"),
    ("Security", "Security")
)

DESIGNATIONS = (
    ("Jr. Executive", "Jr. Executive"),
    ("Sr. Executive", "Sr. Executive"),
    ("Asst. Manager", "Assistant Manager"),
    ("Manager", "Manager"),
    ("Head", "Head"),
    ("GM", "General Manager"),
    ("CEO", "Chief Executive Officer"),
    ("CFO", "Cheif Financial Officer"),
    ("CTO", "Cheif Technical Officer"),
    ("MD", "Managing Director"),
    ("ED", "Executive Director")
)

ASSET_CONDITIONS = (
    ("Fresh", "Fresh"),
    ("Used","Used"),
    ("Damaged", "Damaged")
)

# Employee model that holds information of Employees
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100, primary_key=True)
    employee_contact = models.CharField(max_length=100)
    employee_email = models.EmailField(max_length=100)
    employee_address = models.TextField()
    employee_department = models.CharField(max_length=100,choices=DEPARTMENTS)
    employee_designation = models.CharField(max_length=100,choices=DESIGNATIONS)

    def __str__(self):
        return self.employee_id
    
# Asset model that holds information of Assets
class Asset(models.Model):
    asset_name = models.CharField(max_length=100, choices=ASSET_CHOICES)
    asset_serial = models.CharField(max_length=100)
    asset_manufacturer = models.CharField(max_length=100)
    date_purchased = models.DateTimeField()
    asset_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.asset_name+" "+self.asset_serial
    
# AssetAssignment model that tracks the 
# relationship between assets and employees
class AssetAssignment(models.Model):
    asset=models.ForeignKey(Asset,on_delete=models.PROTECT)
    asset_assigned_to = models.ForeignKey(Employee,on_delete=models.PROTECT)
    asset_assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(default=timezone.now)
    asset_condition_when_assigned = models.CharField(max_length=100,choices=ASSET_CONDITIONS)
    returned_date = models.DateField(null=True, blank=True)
    asset_condition_when_returned = models.CharField(max_length=100,choices=ASSET_CONDITIONS, null=True, blank=True)
    

    def __str__(self):
        return f"{self.asset} assigned to {self.asset_assigned_to} on {self.date_assigned}"

