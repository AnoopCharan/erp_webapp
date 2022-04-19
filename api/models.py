from unicodedata import category
from django.db import models


# Create your models here.
class unitMeasure(models.Model):
    """
    Unit of measurements
    """
    id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=50 ,null=False)

    def __str__(self) -> str:
        return self.unit

class status(models.Model):
    """
    status codes
    """
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50 ,null=False)

class people(models.Model):
    """
    people names and contact
    """
    id = models.AutoField(primary_key= True)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)




class partCategory(models.Model):
    """
    part category for parts
    """
    id=models.AutoField(primary_key=True)
    category = models.CharField(max_length=150 ,verbose_name="part category", null=False)

    def __str__(self) -> str:
        return self.category

class supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150 ,null=False)
    pocName = models.ForeignKey(people, on_delete= models.deletion.CASCADE, related_name='personOfContact')
    address = models.CharField(max_length=300, help_text="Enter full address with country", null=True)

