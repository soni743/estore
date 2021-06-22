from django.db import models
from .product import  Product
from .customer import Customer
from .category import Category
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,default=1)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address=models.CharField(max_length=200,default='',blank=True,null=True)
    phone =models.IntegerField(blank=True,default='',null=True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')

    def Placeorder(self):
        self.save()
