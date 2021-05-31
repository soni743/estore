from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    # To change the display name we will use def __str__() 
    # function in a model. str function in a django model returns
    # a string that is exactly rendered as the display name of 
    # instances for that model.

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
        
    def __str__(self):
        return self.name