from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='cart'
urlpatterns = [
    path('addtocart/', views.addtoCart, name="addtoCart" ),
    path('', views.viewCart, name="viewCart" ),
    path('delete_cart/<slug:id>/', views.delete_cart, name="delete_cart" ),
    path('order/', views.order, name="order" ),
    path('create_order/', views.create_order, name="create_order" ),
    
    
    
    

]