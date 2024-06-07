from django.shortcuts import render,redirect
from Backend.models import Productdb,Categorydb
from WebApp.models import Contactdb,Registerdb,cartdb
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat=Categorydb.objects.all()
    return render(request,"Home.html",{'cat':cat})
def aboutpage(request):
    cat = Categorydb.objects.all()
    return render(request,"About.html",{'cat':cat})
def contactpage(request):
    cat = Categorydb.objects.all()
    return render(request,"Contact.html",{'cat':cat})
def ourproducts(request):
    cat = Categorydb.objects.all()
    pdata=Productdb.objects.all()
    return render(request,"Our_Products.html",{'pdata':pdata,'cat':cat})
def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        ph = request.POST.get('phone')
        obj = Contactdb(Name=na,Email=em,Subject=sub,Message=msg,Mobile=ph)
        obj.save()

        return redirect(contactpage)

def filtered_products(request,cat_name):
    cat = Categorydb.objects.all()
    data=Productdb.objects.filter(Category=cat_name)
    return render(request,"Products_Filtered.html",{'data':data,'cat':cat})

def single_productpage(request,pro_id):
    cat = Categorydb.objects.all()
    data=Productdb.objects.get(id=pro_id)
    return render(request,"Single_Product.html",{'data':data,'cat':cat})
def register_page(request):
    return render(request,"Register.html")

def save_register(request):
    if request.method == "POST":
        na = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pass1')
        cpwd = request.POST.get('pass2')
        obj = Registerdb(Name=na,Email=email,Password=pwd,Confirm_Password=cpwd)
        if Registerdb.objects.filter(Name=na).exists():
            messages.warning(request,"username already exists..!")
            return redirect(register_page)
        elif Registerdb.objects.filter(Email=email).exists():
            messages.warning(request,"email already exists..!")
            return redirect(register_page)
        else:
            obj.save()
            messages.success(request,"Registered Successfully")
            return redirect(userlogin_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if Registerdb.objects.filter(Name=un,Password=pswd) .exists():
            request.session['Name'] = un
            request.session['Password']=pswd
            messages.success(request, "Login Successfully")
            return redirect(homepage)
        else:
            return redirect(register_page)
    else:
        return redirect(register_page)

def userlogout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "User logout Successfully")
    return redirect(homepage)

def save_cart(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pr_name=request.POST.get('pname')
        quant = request.POST.get('quantity')
        tot = request.POST.get('total')
        obj=cartdb(username=un,product_name=pr_name,quantity=quant,totalprice=tot)
        obj.save()
        messages.success(request, "Add to Cart Successfully")
        return redirect(homepage)

def cart_page(request):
    cat = Categorydb.objects.all()
    data=cartdb.objects.filter(username=request.session['Name'])
    total = 0
    for d in data:
        total = total+d.totalprice
    return render(request,"cart.html" ,{'data':data,'cat':cat, 'total':total})

def delete_item(request,p_id):
    x = cartdb.objects.filter(id=p_id)
    x.delete()
    messages.error(request, 'Cart Deleted...!')
    return redirect(cart_page)

def userlogin_page(req):
    return render(req,"userlogin.html")