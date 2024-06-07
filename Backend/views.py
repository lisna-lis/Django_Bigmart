from django.shortcuts import render,redirect
from Backend.models import Categorydb,Productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contactdb
from django.contrib import messages
# Create your views here.
def index_page(request):
    return render(request,"Index.html")
def category_page(request):
    return render(request,"Category.html")
def save_category(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        des=request.POST.get('description')
        img=request.FILES['cimage']
        obj=Categorydb(Category_Name=cname,Description=des,Category_Image=img)
        obj.save()
        messages.success(request,"Category Saved Successfully")
        return redirect(category_page)

def display_category(request):
    data=Categorydb.objects.all()
    return render(request,"Display_Category.html",{'data':data})

def edit_category(request,cid):
    data=Categorydb.objects.get(id=cid)
    return render(request,"Edit_Category.html",{'data':data})

def update_category(request,cid):
    if request.method=="POST":
        cname=request.POST.get('cname')
        des=request.POST.get('description')
        try:
            img=request.FILES['cimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Categorydb.objects.get(id=cid).Category_Image
        Categorydb.objects.filter(id=cid).update(Category_Name=cname,Description=des,Category_Image=file)
        messages.success(request,"Successfully updated")
        return redirect(display_category)
def delete_category(request,cid):
    data=Categorydb.objects.filter(id= cid)
    data.delete()
    messages.error(request,'Category Deleted...!')
    return redirect(display_category)
def login_page(request):
    return render(request,"login_page.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome")
                return redirect(index_page)
            else:
                messages.error(request,"Invalid Password")
                return redirect(login_page)
        else:
            messages.warning(request,"User not found")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Admin logout successfully")
    return redirect(login_page)

def product_page(request):
    cat=Categorydb.objects.all
    return render(request,"Products.html",{'cat':cat})

def save_product(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        pname=request.POST.get('pname')
        pimg=request.FILES['pimage']
        price=request.POST.get('price')
        des=request.POST.get('description')
        obj=Productdb(Category=cname,Product_name=pname,Product_Image=pimg,Price=price,Description=des)
        obj.save()
        messages.success(request,"Product Saved Succesfully")
        return redirect(product_page)

def display_product(request):
    pdata=Productdb.objects.all()
    return render(request,"Display_Product.html",{'pdata':pdata})
def edit_product(request,pid):
    pdata=Productdb.objects.get(id=pid)
    cat=Categorydb.objects.all()
    return render(request,"Edit_Product.html",{'pdata':pdata,'cat':cat})

def update_product(request,pid):
    if request.method=="POST":
        cname=request.POST.get('cname')
        pname=request.POST.get('pname')
        price = request.POST.get('price')
        des = request.POST.get('description')
        try:
            pimg=request.FILES['pimage']
            fs=FileSystemStorage()
            file = fs.save(pimg.name,pimg)
        except MultiValueDictKeyError:
            file=Productdb.objects.get(id=pid).Product_Image
        Productdb.objects.filter(id=pid).update(Category=cname,Product_name=pname,Product_Image=file,Price=price,Description=des)
        messages.success(request,"Products updated")
        return redirect(display_product)

def delete_product(request,pid):
    pdata=Productdb.objects.filter(id=pid)
    pdata.delete()
    messages.error(request,"Product Deleted Successfully")
    return redirect(display_product)
def contact_details(request):
    data=Contactdb.objects.all()
    return render(request,"Contact_Data.html",{'data':data})
def delete_contact(request,conid):
    condata=Contactdb.objects.filter(id=conid)
    condata.delete()
    return redirect(contact_details)