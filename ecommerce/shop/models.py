from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    images=models.ImageField(upload_to="categories")

    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="products")
    desc=models.TextField()
    price=models.FloatField()
    stock=models.IntegerField()
    availabe=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updates=models.DateTimeField(auto_now=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE)

