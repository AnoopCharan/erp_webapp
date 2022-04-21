from django.db import models


# Create your models here.
class UnitMeasure(models.Model):
    """
    Unit of measurements
    """
    id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=50 ,null=False)

    def __str__(self) -> str:
        return self.unit

class Status(models.Model):
    """
    status codes
    """
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50 ,null=False)

    def __str__(self) -> str:
        return self.status

class People(models.Model):
    """
    people names and contact
    """
    id = models.AutoField(primary_key= True)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"

class Attachment(models.Model):
    """
    Attachments for receieving
    """
    id = models.AutoField(primary_key=True)
    fileName = models.CharField(null=False, max_length=150)
    attachedFile = models.FileField(null=False)
    contentType = models.CharField(max_length=150)
    dateOfUpload = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.fileName}.{self.contentType}"


class PartCategory(models.Model):
    """
    part category for parts
    """
    id=models.AutoField(primary_key=True)
    category = models.CharField(max_length=150 ,verbose_name="part category", null=False)

    def __str__(self) -> str:
        return self.category



class Supplier(models.Model):
    """
    Supplier information
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150 ,null=False)
    poc = models.ForeignKey(People, on_delete= models.deletion.CASCADE, related_name='supplierPoc', null=True)
    address = models.CharField(max_length=300, help_text="Enter full address with country", null=True)

    def __str__(self) -> str:
        return self.name

class Part(models.Model):
    """
    Part details
    """
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    category = models.ForeignKey(PartCategory, on_delete=models.deletion.CASCADE, related_name='partCategoryFk')
    supplier = models.ForeignKey(Supplier, on_delete=models.deletion.CASCADE, related_name='supplierFk')

    def __str__(self) -> str:
        return self.name

class MinimumStock(models.Model):
    """
    Minimum stocking level for inventory
    """
    id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Part, on_delete=models.deletion.CASCADE, related_name= "minStockPart")
    minimumStock = models.PositiveIntegerField(null=False)
    lastUpdateDate = models.DateTimeField(auto_now=True)


class StockCurrent(models.Model):
    """
    Current stock levels held in inventory
    """
    id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Part, on_delete=models.deletion.CASCADE, related_name='stockCurrentPart')
    currentStock = models.PositiveIntegerField(null=False)
    lastUpdateDate = models.DateTimeField(auto_now=True)

class Order(models.Model):
    """
    Purchase orders for parts
    """
    id = models.AutoField(primary_key=True)
    poNumber = models.PositiveIntegerField(null=False)
    part = models.ForeignKey(Part, on_delete=models.deletion.CASCADE, related_name='orderPart')
    quantity = models.PositiveIntegerField(null=False)
    unit = models.ForeignKey(UnitMeasure, on_delete=models.deletion.CASCADE, related_name='unitFk')
    dateOrdered = models.DateField(null=False)
    Eta = models.DateField(null=False)
    dateDelivered = models.DateField(null=True)
    status = models.BooleanField(default=False, help_text="order status, true-> delivered, false-> incomplete")

