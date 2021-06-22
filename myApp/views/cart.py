from django.shortcuts import render,redirect
from myApp.models.customer import Customer
# for hashing password
from django.contrib.auth.hashers import check_password
#for classbased views
from django.views import View
from myApp.models import Product


class Cart(View):
    def get(self,request):
        if request.session.get('cart') is not None:
            ids = list(request.session.get('cart').keys())
            product = Product.get_products_by_id(ids)
            print(product)
            return render(request,'cart.html',{'products' : product})
        return redirect('homepage')    

  
   