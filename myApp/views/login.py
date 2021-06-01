from django.shortcuts import render,redirect
from myApp.models.customer import Customer
# for hashing password
from django.contrib.auth.hashers import check_password
#for classbased views
from django.views import View


class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')  
            
        #get email
        customer = Customer.get_customer_by_email(email)
        errormsg=None
        if customer:
            #get password
            userpassword = Customer.objects.get(email = email)
            flag = check_password(password,userpassword.password)
            
            if flag:
                return redirect('homepage')
            else:
                errormsg='Password is Invalid!'
        else:
            errormsg='Email is Invalid!'
            
        formData={
            'Email' : email,
            'error' : errormsg
        }
        return render(request,'login.html',formData)                    


   