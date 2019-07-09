from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from index.models import Poster
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
import csv, io
from django.contrib import messages
from .models import CountryDetails, MyItems, Cart
from project.utils import render_to_pdf
from django.template.loader import get_template
from django.utils import timezone


# Create your views here.
# @login_required(login_url='/account/login/')
def administrator(request):
	totalitems = MyItems.objects.all()

	Trouser_total = MyItems.objects.filter(category="Trouser").count()
	Sales_Trouser_total = Cart.objects.filter(category="Trouser", paid=True).count()
	Trouser_percentage = (Trouser_total/2000)*100

	Shorts_total = Cart.objects.filter(category="Shorts", paid=True).count()
	sales_Shorts_total = MyItems.objects.filter(category="Shorts").count()
	Shorts_percentage = (Shorts_total/2000)*100

	Sales_T_Shirts_total = Cart.objects.filter(category="T-Shirts", paid=True).count()
	T_Shirts_total = MyItems.objects.filter(category="T-Shirts").count()
	T_Shirts_percentage = (T_Shirts_total/2000)*100
	
	Sales_Shoe_total = Cart.objects.filter(category="Shoe", paid=True).count()
	Shoe_total = MyItems.objects.filter(category="Shoe").count()
	Shoe_percentage = (Shoe_total/2000)*100

	sales_Underwear_total = Cart.objects.filter(category="Underwear", paid=True).count()
	Underwear_total = MyItems.objects.filter(category="Underwear").count()
	Underwear_percentage = (Underwear_total/2000)*100

	sales_Singlet_total = Cart.objects.filter(category="Singlet", paid=True).count()
	Singlet_total = MyItems.objects.filter(category="Singlet").count()
	Singlet_percentage = (Singlet_total/2000)*100

	sales_Boxer_total = Cart.objects.filter(category="Boxer", paid=True).count()
	Boxer_total = MyItems.objects.filter(category="Boxer").count()
	Boxer_percentage = (Boxer_total/2000)*100

	sales_Pant_total = Cart.objects.filter(category="Pant", paid=True).count()
	Pant_total = MyItems.objects.filter(category="Pant").count()
	Pant_percentage = (Pant_total/2000)*100

	sales_Socks_total = Cart.objects.filter(category="Socks", paid=True).count()
	Socks_total = MyItems.objects.filter(category="Socks").count()
	Socks_percentage = (Socks_total/2000)*100
	context = { 'sales_Socks_total':sales_Socks_total,'sales_Pant_total':sales_Pant_total,'sales_Boxer_total':sales_Boxer_total,'sales_Singlet_total':sales_Singlet_total,'sales_Underwear_total':sales_Underwear_total,'Sales_Shoe_total':Sales_Shoe_total,'Sales_T_Shirts_total':Sales_T_Shirts_total ,'Shorts_total':Shorts_total ,'Sales_Trouser_total':Sales_Trouser_total, 'totalitems':totalitems, 'Socks_total':Socks_total, 'Socks_percentage':Socks_percentage,'Pant_total':Pant_total, 'Pant_percentage':Pant_percentage, 'Boxer_total':Boxer_total, 'Boxer_percentage':Boxer_percentage, 'Singlet_total':Singlet_total, 'Singlet_percentage':Singlet_percentage, 'Underwear_total':Underwear_total, 'Underwear_percentage':Underwear_percentage, 'Shoe_total':Shoe_total, 'Shoe_percentage':Shoe_percentage, 'T_Shirts_total':T_Shirts_total, 'T_Shirts_percentage':T_Shirts_percentage, 'Trouser_percentage':Trouser_percentage,'Trouser_total':Trouser_total, 'Trouser_percentage':Trouser_percentage, 'Shorts_total':Shorts_total, 'Shorts_percentage':Shorts_percentage}
	# post_active_total = Poster.objects.filter(active=True).count()
	# post_active_total_percentage = (post_active_total/10000)*100

	# post_disabled_total = Poster.objects.filter(active=False).count()
	# post_disabled_total_percentage = (post_disabled_total/10000)*100

	# total_post = Poster.objects.all().count()
	# total_post_percentage = (total_post/10000)*100
	#context = {'totalitems':totalitems, 'total_post_percentage':total_post_percentage, 'post_disabled_total_percentage':post_disabled_total_percentage,'post_active_total_percentage':post_active_total_percentage, 'user_total_percentage':user_total_percentage, 'user_total':user_total, 'post_active_total':post_active_total, 'post_disabled_total':post_disabled_total, 'total_post':total_post}
	return render(request, 'Administrator/index.html', context)

# @login_required(login_url='/account/login/')
def userpostsview(request):
	qs = MyItems.objects.all()
	context = {"qs":qs}
	return render(request, 'Administrator/products.html', context)

def addtoCart(request):
	post_pk = request.POST.get("post_pk")
	qty1 = request.POST.get("qty")
	qty = int(qty1)
	qs = MyItems.objects.get(pk=post_pk)
	Cart.objects.create(category=qs.category, description=qs.description, qty=qty, price=qs.price*qty, single_price=qs.price, date=timezone.now())
	cart = Cart.objects.filter(paid=False).count()
	total_price1 = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price1:
		a = a+i.price
	return JsonResponse({"cart_total":cart, 'id':post_pk, 'total_price':a, 'qty':qty})


def editCart(request):
	post_pk = request.POST.get("post_pk")
	qty1 = request.POST.get("qty")
	qty = int(qty1)
	print('qty', qty)
	qs = Cart.objects.get(pk=post_pk)
	qs.price = qs.single_price * qty
	qs.qty = qty
	qs.save()
	cart = Cart.objects.filter(paid=False).count()
	total_price1 = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price1:
		a = a+i.price
	print(qs.single_price)
	return JsonResponse({"cart_total":cart, 'id':post_pk, 'total_price':a, 'qty':qty, 'price':qs.price, 'single_price':qs.single_price})

def deleteCart(request):

	post_pk = request.POST.get("post_pk")
	qs = Cart.objects.get(pk=post_pk)
	qs.delete()
	cart = Cart.objects.filter(paid=False).count()
	total_price1 = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price1:
		a = a+i.price
	return JsonResponse({"cart_total":cart, 'id':post_pk, 'total_price':a})


def cart(request):
	qs = Cart.objects.filter(paid=False)
	return render(request, 'Administrator/cart.html', {"qs":qs})

def mysales(request):
	qs = Cart.objects.filter(paid=True)
	return render(request, 'Administrator/mysales.html', {"qs":qs})

def viewDetails(request):
	post_pk = request.POST.get("post_pk")
	post = Poster.objects.get(id_user=post_pk)
	data = serializers.serialize('json', [post])
	return JsonResponse({"data":data})

def additems(request):
	category = request.POST.get("category")
	description = request.POST.get("description")
	price = request.POST.get("price")
	stock = request.POST.get("stock")
	newitem = MyItems.objects.create(category=category, description=description, price=price, stock=stock)
	newitem.save()
	print('id', newitem.id)


	return JsonResponse({"category":category, 'description':description, 'price':price, 'stock':stock, 'product_id':newitem.id})


def editItems(request):
	category = request.POST.get("category")
	description = request.POST.get("description")
	price = request.POST.get("price")
	stock = request.POST.get("stock")
	product_id = request.POST.get("product_id")
	myitems = MyItems.objects.get(pk=product_id)
	myitems.category = category
	myitems.description = description
	myitems.price = price
	myitems.stock = stock
	myitems.save()

	return JsonResponse({"category":category, 'description':description, 'price':price, 'stock':stock, 'product_id':product_id})


def deletemyItems(request):
	product_id = request.POST.get('product_id')
	item = MyItems.objects.get(id=product_id)
	item.delete()
	return JsonResponse({'product_id':product_id})



@permission_required('admin.can_add_log_entry')
def upload_csv(request):
	if request.method == 'GET':
		return render(request, 'Administrator/upload_csv.html')
	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, "This is not a csv file")
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		print(column[0], column[1], column[2], column[3], column[4], column[5], column[6])
		_, created = CountryDetailsTest.objects.update_or_create(
			postcode = column[0],
			suburb = column[1],
			state = column[2],
			dc = column[3],
			detail_type = column[4], 
			lat = column[5],
			ion = column[6],			
			)
	context = {}
	return HttpResponse("done")

def generatePdf(request):
	total_cart = Cart.objects.filter(paid=False).count()
	total_price = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price:
		a = a+i.price
	qs = Cart.objects.filter(paid=False)
	template = get_template('Administrator/order.html')
	context={'qs':qs, 'total_cart':total_cart, 'total_price':a}
	html = template.render(context)
	pdf = render_to_pdf('Administrator/order.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')

		filename = "%s_receipt.pdf" %('1k-clothes')
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")


def pay(request):
	sum = 0
	name = request.POST.get('name')
	phone = request.POST.get('phone')
	cart = Cart.objects.filter(paid=False)
	for i in cart:
		i.name = name
		cart1 = Cart.objects.get(paid=False, category=i.category, description=i.description, pk=i.pk)
		
		# for i in cart1:
		# 	sum = sum + i.qty
		

		myItems = MyItems.objects.get(category=i.category, description=i.description)
		# print('aa',myItems.stock)

		myItems.stock = myItems.stock - cart1.qty
		
		myItems.save()
		# print('bb',cart1.qty, myItems.stock)
		i.phonenumber = phone 
		i.paid = True
		i.date = timezone.now()
	
		i.save()
	total_cart = Cart.objects.filter(paid=False).count()
	total_price = Cart.objects.filter(paid=True, name=name, phonenumber=phone)
	a = 0
	for i in total_price:
		a = a+i.price
	qs = Cart.objects.filter(paid=True, name=name, phonenumber=phone)
	
	template = get_template('Administrator/order.html')
	context={'qs':qs, 'total_cart':total_cart, 'total_price':a, 'name':name, 'phonenumber':phone}
	html = template.render(context)
	pdf = render_to_pdf('Administrator/order.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')

		filename = "%s_receipt.pdf" %('1k-clothes')
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")


