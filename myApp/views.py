from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# for hashing password
from django.contrib.auth.hashers import make_password,check_password
#for classbased views
from django.views import View

def ValidateUsers(customer):
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

def RegisteredUsers(request):
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
    errormsg = ValidateUsers (customer)

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

def signup(request):
    if(request.method=='GET'):
        return render(request,'signup.html')
    else:
        return RegisteredUsers(request)

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
    data={}
    data['products'] = item
    data['categories'] = category
    return render(request,'index.html',data)

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        return CheckLogin(request)         

# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     else:
#         return CheckLogin(request)
          
def CheckLogin(request):
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