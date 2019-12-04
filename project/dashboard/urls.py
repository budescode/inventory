from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='dashboard'
urlpatterns = [

    path('', views.dashboard, name="dashboard" ),
    path('ordered_delivery/', views.ordered_delivery, name="ordered_delivery" ),
    path('delete_order/<slug:id>/', views.delete_order, name="delete_order" ),
    path('search_order_id/', views.search_order_id, name="search_order_id" ),


    path('order_delivery_details/<slug:id>/', views.order_delivery_details, name="order_delivery_details" ),
    path('order_pending_delivery_change/<slug:id>/', views.order_pending_delivery_change, name="order_pending_delivery_change" ),
    path('order_delivered_change/<slug:id>/', views.order_delivered_change, name="order_delivered_change" ),
    path('filter_sold/', views.filter_sold, name="filter_sold" ),


    path('todaysreportorder/', views.todaysreportorder, name="todaysreportorder" ),
    path('weeklyreportorder/', views.weeklyreportorder, name="weeklyreportorder" ),
    path('monthlyreportorder/', views.monthlyreportorder, name="monthlyreportorder" ),
    path('yearlyreportorder/', views.yearlyreportorder, name="yearlyreportorder" ),

    path('todaysreportsold/', views.todaysreportsold, name="todaysreportsold" ),
    path('weeklyreportsold/', views.weeklyreportsold, name="weeklyreportsold" ),
    path('monthlyreportsold/', views.monthlyreportsold, name="monthlyreportsold" ),
    path('yearlyreportsold/', views.yearlyreportsold, name="yearlyreportsold" ),

    path('category/', views.category, name="category" ),
    path('deletecategory/<slug:id>/', views.deletecategory, name="deletecategory" ),

    path('subcategory/', views.subcategory, name="subcategory" ),
    path('deletesubcategory/<slug:id>/', views.deletesubcategory, name="deletesubcategory" ),

    path('filter_items/<slug:categoryid>/<slug:subcategoryid>/<slug:sex>/<slug:size>/', views.filter_items, name="filter_items" ),
    path('delete_items/<slug:categoryid>/<slug:subcategoryid>/<slug:sex>/<slug:id>/<slug:size>/', views.delete_items, name="delete_items" ),
    path('add_items/<slug:id>/', views.additem, name="add_item" ),



]


