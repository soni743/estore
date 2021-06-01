from django.shortcuts import render,redirect
from myApp.models.customer import Customer
# for hashing password
from django.contrib.auth.hashers import make_password
#for classbased views
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request): 
        postData  = request.POST
        customer = Customer(
            firstname = postData.get('firstname'),
            lastname  = postData.get('lastname'),
            phone = postData.get('phone'),
            email = postData.get('email'),
            password = postData.get('password')
        )
        formValue={
                'first_name' : customer.firstname,
                'last_name' : customer.lastname,
                'phone' : customer.phone,
                'email' : customer.email,
                'password' : customer.password
        }
            
        errormsg =None
        errormsg = self.ValidateUsers (customer)

        context={
            'error' : errormsg,
            'formData' : formValue
        }    


        if not errormsg:
            customer.password = make_password(customer.password)
            customer.Register()
            errormsg ='Customer Added successfully!' 
            return redirect('homepage') 
  
        return render(request,'signup.html', context) 
   
    def ValidateUsers(self,customer):
        errormsg=None
        if (not customer.firstname):
            errormsg ='Firstname required'
        elif len(customer.firstname) < 4:
            errormsg ='Firstname must be 4 or more characters long'
        elif (not customer.lastname):
            errormsg ='Lastname required'
        elif len(customer.lastname) < 4:
            errormsg ='Lastname must be 4 or more characters long'  
        elif (not customer.phone):
            errormsg ='Phone required'
        elif len(customer.phone) < 10:
            errormsg ='Phone must be 10 digits long'                     
        elif (not customer.email):
            errormsg ='Email required'
        elif (not customer.password):
            errormsg ='Password required'
        elif customer.isExits():
            errormsg = 'Email is Already registered'
        return errormsg
