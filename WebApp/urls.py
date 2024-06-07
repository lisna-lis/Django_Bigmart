from django.urls import path
from WebApp import views
urlpatterns=[
    path('',views.homepage,name="Home"),
    path('About/',views.aboutpage,name="About"),
    path('ContactUs/',views.contactpage,name="ContactUs"),
    path('OurProducts/',views.ourproducts,name="OurProducts"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('single_productpage/<int:pro_id>/',views.single_productpage,name="single_productpage"),
    path('register_page/',views.register_page,name="register_page"),
    path('save_register/',views.save_register,name="save_register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),
    path('userlogin_page/', views.userlogin_page, name="userlogin_page"),


]