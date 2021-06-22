from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models.product import Product
from myApp.models.orders import Order
from myApp.models.customer import Customer

#for classbased views
from django.views import View

class Checkout(View):
    def post (self, request):
      address = request.POST.get('address')
      phone = request.POST.get('phone')
      cart = request.session.get('cart')
      customer = request.session.get('customer')
      products =  Product.get_products_by_id(list(cart.keys()))
      print(address,phone,cart,customer,products)
      for product in products:
        order = Order(
          customer = Customer(id = customer),
          product = product,
          price= product.price,
          address =address,
          phone = phone,
          quantity = cart.get(str(product.id))
        )
        order.Placeorder()
       
       
      return redirect('orderpage')