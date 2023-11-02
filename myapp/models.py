from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name + ',' + str(self.age)
    

class Customer(models.Model):
        customer_code = models.BigAutoField(max_length=10, primary_key=True, serialize=False)
        username = models.CharField(max_length=100, null=True)
        address = models.CharField(blank=True, max_length=100, null=True)
        tel_number = models.CharField(max_length=100, null=True)
        def __str__(self):
            return self.username + ',' + self.address + ',' + self.tel_number
        
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    employee_name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=1000, null=True)
    sex = models.CharField(max_length=10, null=True)
    salary = models.FloatField(blank=True, null=True)
    tel_number = models.CharField(max_length=10, null=True)
    address = models.CharField(blank=True, max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

class Membership(models.Model):
    customer_code = models.CharField(max_length=10, primary_key=True, serialize=False)
    member_point = models.CharField(max_length=1000,null=True)
    member_level = models.CharField(max_length=10,null=True)

class Order(models.Model):
    order_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    order_date = models.DateField(null=True)
    customer_id = models.CharField(max_length=10)
    total = models.IntegerField(null=True)

class OrderLineItem(models.Model):
    order_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    order_item_id = models.CharField(max_length=10)
    product_id = models.CharField(max_length=10,)
    order_quantity = models.IntegerField(null=True)
    total_order_price = models.FloatField(null=True)

class Pet(models.Model):
    pet_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    customer_id = models.CharField(max_length=10)
    pet_name = models.CharField(max_length=100,)
    pet_type = models.CharField(max_length=10,null=True)

class Product(models.Model):
    product_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    product_name = models.CharField(max_length=100, null=True)
    product_brand =  models.CharField(max_length=100, null=True)
    product_price = models.FloatField(null=True)
    product_quantity = models.IntegerField(null=True)
    product_category = models.CharField(max_length=100, null=True)
    pet_type = models.CharField(max_length=10,null=True)
    product_pic = models.FilePathField(null=True)

class Receipt(models.Model):
    receipt_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    receipt_date = models.DateField(null=True)
    total_receipt_amount = models.FloatField(null=True)
    payment_method =  models.CharField(max_length=10,null=True)
    reward_id = models.CharField(max_length=10,null=True)
    payment_reference = models.CharField(max_length=100,null=True)
    customer_id = models.CharField(max_length=10,null=True)

class Reward(models.Model):
    reward_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    reward_name  = models.CharField(max_length=10)
    require_point =  models.FloatField(max_length=1000,null=True)
    description = models.CharField(max_length=100)