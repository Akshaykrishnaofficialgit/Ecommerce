from django.db import models
from shop.models import Products
from django.contrib.auth.models import User
class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.product.price*self.quantity


    def __str__(self):
        return self.product.name

class Order_details(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    adrress=models.TextField()
    phone=models.BigIntegerField()
    pin=models.IntegerField()
    order_id=models.CharField(max_length=50)
    payment_status=models.CharField(max_length=50,default="Pending")
    delivery_status=models.CharField(max_length=50,default="pending")
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

class Payment_table(models.Model):
    name=models.CharField(max_length=50)
    amount=models.FloatField()
    order_id = models.CharField(max_length=50)
    rayzorpay_payment_id=models.CharField(max_length=50,blank=True)
    payment=models.BooleanField(default=False)

    def __str__(self):
        return self.order_id