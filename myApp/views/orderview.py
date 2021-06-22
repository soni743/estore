from django.shortcuts import render,redirect
# for hashing password
from django.contrib.auth.hashers import check_password
#for classbased views
from django.views import View
from myApp.models.orders import Order

# from django.utils.decorators import method_decorator

class Orders(View):

    # @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orderData = Order.get_orders_by_customer(customer)
        print(orderData)
        return render(request,'order.html',{'orders' : orderData})    
       
  
   