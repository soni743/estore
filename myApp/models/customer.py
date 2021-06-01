from django.db import models
from django.contrib.auth.hashers import check_password

class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def Register(self):
        self.save()

    def isExits(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False    

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email = email)
        except:
            return False            