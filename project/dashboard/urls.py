from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='dashboard'
urlpatterns = [

    path('', views.dashboard, name="dashboard" ),
    path('ordered_delivery/', views.ordered_delivery, name="ordered_delivery" ),
    path('order_delivery_details/<slug:id>/', views.order_delivery_details, name="order_delivery_details" ),
    path('order_pending_delivery_change/<slug:id>/', views.order_pending_delivery_change, name="order_pending_delivery_change" ),
    path('order_delivered_change/<slug:id>/', views.order_delivered_change, name="order_delivered_change" ),
    
    path('todaysreportorder/', views.todaysreportorder, name="todaysreportorder" ),
    path('todaysreportsold/', views.todaysreportsold, name="todaysreportsold" ),
    path('category/', views.category, name="category" ),
    path('deletecategory/<slug:id>/', views.deletecategory, name="deletecategory" ),

    path('subcategory/', views.subcategory, name="subcategory" ),
    path('deletesubcategory/<slug:id>/', views.deletesubcategory, name="deletesubcategory" ),
    
    path('filter_items/<slug:unisex>/<slug:categoryid>/<slug:subcategoryid>/<slug:size>/', views.filter_items, name="filter_items" ),
    path('delete_items/<slug:unisex>/<slug:categoryid>/<slug:subcategoryid>/<slug:size>/<slug:id>/', views.delete_items, name="delete_items" ),
        

]