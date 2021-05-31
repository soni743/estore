from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.
def Index(request):
    item = None
    category = Category.get_all_categories()
    
    #get categoryid 
    category_id = request.GET.get('categoryid')
    if category_id:
        item = Product.getProductbyCategoryId(category_id)       
    else:
        item = Product.getAllProducts()
    # if int(category_id) == 0:
    #     item = Product.getAllProducts()        
    # elif category_id is not None:        
    #     item = Product.getProductbyCategoryId(category_id)
    # else:
    #     item = Product.getAllProducts()        

    data={}
    data['products'] = item
    data['categories'] = category
    return render(request,'index.html',data)