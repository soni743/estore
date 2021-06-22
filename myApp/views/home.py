from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models.product import Product
from myApp.models.category import Category

#for classbased views
from django.views import View

class Home(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = cart
           
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

    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product) #check qunatity of perticular product
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product]= quantity - 1    
                else:    
                    cart[product]= quantity + 1
            else:
                cart[product]= 1
        else:  #if cart is none, create new dictionary of cart
            cart={}
            cart[product]=1           

        request.session['cart'] = cart
        print(request.session['cart'])
            
        return redirect('homepage')