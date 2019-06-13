from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)


class Customer(models.Model):
    name = models.CharField(max_length=200)


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=True)


class OrderDetails(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
