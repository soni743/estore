from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models.product import Product
from myApp.models.category import Category

#for classbased views
from django.views import View

class Home(View):
    def get(self, request):
        item = None
        category = Category.get_all_categories()
        
        #get categoryid 
        category_id = request.GET.get('categoryid')
        if category_id:
            item = Product.getProductbyCategoryId(category_id)       
        else:
            item = Product.getAllProducts()
        data={}
        data['products'] = item
        data['categories'] = category
        return render(request,'index.html',data)
        