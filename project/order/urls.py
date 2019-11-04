from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='order'
urlpatterns = [

    path('', views.myorder, name="myorder" ),
    path('deletemyorder/<slug:id>/', views.deletemyorder, name="deletemyorder" ),
    path('orderdetails/<slug:id>/', views.orderdetails, name="orderdetails" ),
    path('deletemyordereditems/<slug:id>/<slug:order_id>/', views.deletemyordereditems, name="deletemyordereditems" ),






]