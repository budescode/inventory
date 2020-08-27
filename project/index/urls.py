from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='home'
urlpatterns = [
    path('', views.home, name="home" ),
	path('about/', views.about, name="about" ),
	path('terms/', views.terms, name="terms" ),
	path('faq/', views.faq, name="faq" ),
	path('search/', views.search, name="search" ),
	path('customer_service/', views.customer_service, name="customer_service" ),
	path('orders_and_returns/', views.orders_and_returns, name="orders_and_returns" ),

	path('contact/', views.contact, name="contact" ),
	path('detail/<slug:id>/', views.detail, name="detail" ), #this is the url for the detail page
	path('category/<slug:id>/', views.filter_category, name="filter_category" ), #this will filter category by id
	path('subcategory/<slug:id>/', views.filter_subcategory, name="filter_subcategory" ), #this will filter subcategory by id
	path('filter/<slug:category>/<slug:unisex>/', views.filter_unisex_category, name="filter_unisex_category" ), #this will
	#filter category by unisex(male, female, boys, girls)
	path('list/<slug:category>/<slug:subcategory>/<slug:unisex>/', views.filter_unisex_subcategory, name="filter_unisex_subcategory" ),
	path('filtersearch_unisex_subcategory/', views.filtersearch_unisex_subcategory, name="filtersearch_unisex_subcategory" ),

	#filter category and subcategory unisex(male, female, boys, girls)
	path('filter_allcategory/<slug:name>/', views.filter_allcategory, name="filter_allcategory" ),
	path('filtersearch_allcategory/', views.filtersearch_allcategory, name="filtersearch_allcategory" ),

	path('filter_male/', views.filter_male, name="filter_male" ),

	path('addtoFavourite/<slug:id>/', views.addtoFavourite, name="addtoFavourite" ),
	path('myFavourite/', views.myFavourite, name="myFavourite" ),
	path('careers/', views.careers, name="careers" ),
	path('store/', views.store, name="store" ),
	path('availableposition/', views.availableposition, name="availableposition" ),
	path('application/', views.application, name="application" ),

	path('deletemyFavourite/<slug:id>/', views.deletemyFavourite, name="deletemyFavourite" ),

	#filter category and subcategory unisex(male, female, boys, girls)

]



