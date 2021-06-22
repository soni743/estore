from django.shortcuts import render,redirect, HttpResponseRedirect
from myApp.models.customer import Customer
# for hashing password
from django.contrib.auth.hashers import check_password
#for classbased views
from django.views import View


class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
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
            request.session['email'] = email
            #get customer id
            request.session['customer'] = userpassword.id
            flag = check_password(password,userpassword.password)
            if flag:

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')
            else:
                errormsg='Password is Invalid!'
        else:
            errormsg='Email is Invalid!'

        print(customer)    
       
        
        formData={
            'Email' : email,
            'error' : errormsg
        }
        return render(request,'login.html',formData)                    

def logout(request):
    request.session.clear()
    return redirect('login')
   