from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username
        
    class Meta():
        db_table = "User"

class ProductTypes(models.Model):
    id_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    def __str__(self):
        return str(self.id_type) + " - " + self.name
    class Meta():
        db_table = "Type of product"

class Cake(models.Model):
    id_cake = models.AutoField(primary_key=True)
    size = models.CharField(max_length=50, default='Grande')
    bread = models.CharField(max_length=100, default='')
    fill = models.CharField(max_length=100, default='')
    isThreeMilk = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id_cake) + " - " + self.size + ": Pan sabor " + self.bread + ' con relleno de ' + self.fill
    class Meta():
        db_table = "Cake"

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    typeOfProduct = models.ForeignKey(ProductTypes, on_delete = models.CASCADE)
    id_cake = models.ForeignKey(Cake, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id_product) + " - " + self.name
    class Meta():
        db_table = "Product"

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, default='')
    email = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return str(self.id_client) + " - " + self.name
    class Meta():
        db_table = "Client"

class Buy(models.Model):
    id_buy = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(auto_now=True)
    total = models.FloatField(default=0)
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id_buy)
    class Meta():
        db_table = "Buy"

class ItemsBuy(models.Model):
    id_buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    class Meta():
        db_table = "Items - Buy"
    def __str__(self):
        return str(self.id_buy.date.strftime("%d/%m/%Y")) + " - " + str(self.id_buy.id_client.name) + " - " + str(self.id_product.name)



