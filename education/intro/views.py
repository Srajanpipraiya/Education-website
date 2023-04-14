import re,os
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def home(request):
    # context = {
    #     'variable':"A Wonderful path for your future"
    # }
    return render(request,'intro/home.html')
    # return HttpResponse("Hello, Welcome to my website Please click on below link to go to next page")

# def welcome(request, name):
#     return render(
#         request,
#         'intro/welcome.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )
def index(request):
    # context = {
    #     'variable':"this is sent"
    # }
    return render(request,'intro/index.html')
def info(request):
    return render(request,'intro/info.html')
# def orders(request):
#     return render(request,'intro/orders.html')
# def product(request):
#     return render(request,'intro/product.html')
# def purchase(request):
#     return render(request,'intro/purchase.html')
def contact(request):
    return render(request,'intro/contact.html')

# class ProductView(View):
#     def get(self,request):
#         topwears = Product.objects.filter(category='TW')
#         bottomwears = Product.objects.filter(category='BW')
#         mobiles = Product.objects.filter(category='M')
#         return render(request,'intro/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})

        
# class ProductDetailView(View):
#     def get(self,request,pk):
#         product=Product.objects.get(pk=pk)
#         item_already_in_cart=False
#         if request.user.is_authenticated:
#             item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
#         return render(request,'intro/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})

# @login_required
# def add_to_cart(request):
#     user=request.user
#     product_id = request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Cart(user=user, product=product).save()
#     return redirect('/cart')

# @login_required
# def show_cart(request):
#     if request.user.is_authenticated:
#         user=request.user
#         cart=Cart.objects.filter(user=user)
#         # print(cart)
#         amount=0.0
#         shipping_amount = 70.0
#         total_amount = 0.0
#         cart_product = [p for p in Cart.objects.all() if p.user == user ]
#         # print(cart_product)
#         if cart_product:
#             for p in cart_product:
#                 tempamount = (p.quantity*p.product.discounted_price)
#                 amount+=tempamount
#                 total_amount= amount+shipping_amount
#             return render(request, 'intro/addtocart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})
#         else:
#             return render(request, 'intro/emptycart.html')

# def plus_cart(request):
#     if request.method == "GET":
#         prod_id = request.GET['prod_id']
#         c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#         c.quantity+=1
#         c.save()
#         amount=0.0
#         shipping_amount=70.0
#         cart_product = [p for p in Cart.objects.all() if p.user == request.user ]
#         for p in cart_product:
#             tempamount = (p.quantity*p.product.discounted_price)
#             amount+=tempamount
#             totalamount= amount+shipping_amount
#         data = {
#             'quantity':c.quantity,
#             'amount':amount,
#             'totalamount':totalamount
#         }
#         # print(data)
#         return JsonResponse(data)

# def minus_cart(request):
#     if request.method == "GET":
#         prod_id = request.GET['prod_id']
#         c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#         if c.quantity>1:
#             c.quantity-=1
#             c.save()
#             amount=0.0
#             shipping_amount=70.0
#             cart_product = [p for p in Cart.objects.all() if p.user == request.user ]
#             for p in cart_product:
#                 tempamount = (p.quantity*p.product.discounted_price)
#                 amount+=tempamount
#             data = {
#             'quantity':c.quantity,
#             'amount':amount,
#             'totalamount':amount+shipping_amount
#             }
#             return JsonResponse(data)

# def remove_cart(request):
#     if request.method == "GET":
#         prod_id = request.GET['prod_id']
#         c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#         c.delete()
#         amount=0.0
#         shipping_amount=70.0
#         cart_product = [p for p in Cart.objects.all() if p.user == request.user ]
#         for p in cart_product:
#             tempamount = (p.quantity*p.product.discounted_price)
#             amount+=tempamount
#         data = {
#             'amount':amount,
#             'totalamount':amount+shipping_amount
#         }
#         # print(data)
#         return JsonResponse(data)
# @login_required
# def buy_now(request):
#  return render(request, 'intro/buynow.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'intro/address.html',{'add':add,'active':'btn-primary'})

# @login_required
# def orders(request):
#     op=OrderPlaced.objects.filter(user=request.user)
#     return render(request, 'intro/orders.html',{'order_placed':op})


# def mobile(request,data=None):
#     if data==None:
#         mobiles = Product.objects.filter(category='M')
#     elif data == 'Redmi' or data == 'Samsung' or data == 'Vivo' or data == 'Oppo' or data == 'Realme' or data == 'Iphone' or data == 'Nokia' or data == 'Techno':
#         mobiles = Product.objects.filter(category='M').filter(brand=data)
#     elif data == 'Below':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
#     elif data == 'Above':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
#     return render(request, 'intro/mobile.html',{'mobiles':mobiles})


# def topwear(request,data=None):
#     if data==None:
#         topwears = Product.objects.filter(category='TW')
#     elif data == 'Full-shirt' or data == 'Half-shirt' or data == 'T-shirt' or data == 'Other':
#         topwears = Product.objects.filter(category='TW').filter(brand=data)
#     elif data == 'Below':
#         topwears = Product.objects.filter(category='TW').filter(discounted_price__lt=500)
#     elif data == 'Above':
#         topwears = Product.objects.filter(category='TW').filter(discounted_price__gt=500)
#     return render(request, 'intro/topwear.html',{'topwears':topwears})

# def bottomwear(request,data=None):
#     if data==None:
#         bottomwears = Product.objects.filter(category='BW')
#     elif data == 'Jeans' or data == 'Formal' or data == 'Casual' or data == 'Nikkar' or data == 'Other':
#         bottomwears = Product.objects.filter(category='BW').filter(brand=data)
#     elif data == 'Below':
#         bottomwears = Product.objects.filter(category='BW').filter(discounted_price__lt=500)
#     elif data == 'Above':
#         bottomwears = Product.objects.filter(category='BW').filter(discounted_price__gt=500)
#     return render(request, 'intro/bottomwear.html',{'bottomwears':bottomwears})

def login(request):
 return render(request, 'intro/login.html')


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'intro/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! You Are Registered Successfully')
            form.save()
        return render(request,'intro/customerregistration.html',{'form':form})

# @login_required
# def checkout(request):
#     user=request.user
#     add = Customer.objects.filter(user=user)
#     cart_items = Cart.objects.filter(user=user)
#     amount=0.0
#     shipping_amount=70.0
#     totalamount=0.0
#     cart_product = [p for p in Cart.objects.all() if p.user == request.user ]
#     for p in cart_product:
#         tempamount = (p.quantity*p.product.discounted_price)
#         amount+=tempamount
#     totalamount= amount+shipping_amount
        
#     return render(request, 'intro/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})

# @login_required
# def payment_done(request):
#     user=request.user
#     custid = request.GET.get('custid')
#     customer = Customer.objects.get(id=custid)
#     cart= Cart.objects.filter(user=user)
#     for c in cart:
#         OrderPlaced(user=user,customer=customer,product=c.product, quantity=c.quantity).save()
#         c.delete()
#     return redirect("orders")

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'intro/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg= Customer(user=usr,name=name, locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulation!! Profile Updated Successfully')
        return render(request, 'intro/profile.html',{'form':form,'active':'btn-primary'})

    def saveEnquiry(self,request):
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            website=request.POST.get('website')
            message=request.POST.get('message')
            en=contactEnquiry(name=name,email=email, phone=phone)
            en.save()
            n="Data Inserted"
        return render(request,"intro/contact.html",{'n':n})
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # # Filter the name argument to letters only using regular expressions. URL arguments
    # # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return HttpResponse(content)