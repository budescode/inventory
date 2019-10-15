from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='administrator'
urlpatterns = [
    path('', views.administrator, name="administrator" ),
	path('products/', views.userpostsview, name="products" ),
	path('dailyreport/', views.dailyReportView, name="dailyreport" ),
	path('weeklyreport/', views.weeklyreport, name="weeklyreport" ),
	path('yearlyreport/', views.yearlyreport, name="yearlyreport" ),
	path('monthlyreport/', views.monthlyreport, name="monthlyreport" ),
	path('comparereport/', views.comparereport, name="comparereport" ),
	path('filter_index/', views.filter_index, name="filter_index" ),
	path('editmyitems/', views.editmyitems, name="editmyitems" ),





    path('todaysreport/', views.todaysreport, name="todaysreport" ),

	path('addtocart/', views.addtoCart, name="addtocart" ),
	path('addtocategory/', views.addtoCategory, name="addtocategory" ),
	path('addsubcategory/', views.addSubCategory, name="addsubcategory" ),

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
# 	path('', views.home, name="home" ),
    path('pettycash/', views.pettyCash, name="pettycash" ),
    path('addpettycash/', views.addpettyCash, name="addpettycash" ),
    path('deletepettycash/<slug:id>/', views.delete_pettycash, name="deletepettycash" ),
    path('editpettycash/<slug:id>/', views.edit_pettycash, name="editpettycash" ),
    path('category/', views.category, name="category" ),
    path('deletecategory/<slug:id>/', views.deletecategory, name="deletecategory" ),

    path('deletesubcategory/<slug:id>/', views.deletesubcategory, name="deletesubcategory" ),

    path('subcategory/', views.subcategory, name="subcategory" ),
    # path('deletecategory/<slug:id>/', views.deletecategory, name="deletecategory" ),





]

