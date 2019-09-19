from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='administrator'
urlpatterns = [
    path('administrator/', views.administrator, name="administrator" ),
	path('products/', views.userpostsview, name="products" ),
	path('dailyreport/', views.dailyReportView, name="dailyreport" ),
	path('addtocart/', views.addtoCart, name="addtocart" ),
	path('addtocategory/', views.addtoCategory, name="addtocategory" ),

	path('viewdetails/', views.viewDetails, name="viewdetails" ),
	path('upload/', views.upload_csv, name="upload_csv" ),
	path('cart/', views.cart, name="cart" ),
	path('deletecart/<slug:id>/<slug:product_id>/', views.deleteCart, name="deletecart" ),
	path('editcart/', views.editCart, name="editcart" ),
	path('generatePdf/', views.generatePdf, name="generatePdf" ),
	path('pay/', views.pay, name="pay" ),
	path('mysales/', views.mysales, name="mysales" ),
	path('edititems/', views.editItems, name="edititems" ),
	path('deletemyitems/', views.deletemyItems, name="deletemyitems" ),
	path('additems/', views.additems, name="additems" ),
	path('filtersales/', views.filtersales, name="filtersales" ),
	path('deleteallcart/', views.deleteAllCart, name="deleteallcart" ),
	path('', views.home, name="home" ),
    path('pettycash/', views.pettyCash, name="pettycash" ),
    path('addpettycash/', views.addpettyCash, name="addpettycash" ),
    path('deletepettycash/<slug:id>/', views.delete_pettycash, name="deletepettycash" ),
    path('editpettycash/<slug:id>/', views.edit_pettycash, name="editpettycash" ),
    path('category/', views.category, name="category" ),



]

