from django.shortcuts import render, get_object_or_404, redirect
from index.models import Index, IndexSize, IndexCategory, IndexSubCategory
from django.http import HttpResponse
from cart.models import Cart
from order.models import Order
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from datetime import datetime, timedelta, date
from .forms import IndexForm, IndexCategoryForm, IndexSubCategoryForm



def dashboard(request):
	category = IndexCategory.objects.all()
	subcategory = IndexSubCategory.objects.all()
	total_items = Index.objects.all()

	men_total = 0
	men = IndexCategory.objects.filter(unisex__iexact='Men')
	for i in men:
		men_total = men_total + i.total_count


	women_total = 0
	women = IndexCategory.objects.filter(unisex__iexact='Women')
	for i in women:
		women_total = women_total + i.total_count

	boys_total = 0
	boys = IndexCategory.objects.filter(unisex__iexact='Boys')
	for i in boys:
		boys_total = boys_total + i.total_count

	girls_total = 0
	girls = IndexCategory.objects.filter(unisex__iexact='Girls')
	for i in girls:
		girls_total = girls_total + i.total_count
	unisex = [{"name": "Men", 'total_count':men_total},{"name": "Women", 'total_count':women_total}, {"name": "Boys", 'total_count':boys_total}, {"name": "Girls", 'total_count':girls_total}]
	context = {'category':category, 'subcategory':subcategory, 'unisex':unisex, 'men_total':men_total, 'women_total':women_total,
	'boys_total':boys_total, 'girls_total':girls_total, 'total_items':total_items
	}
	return render(request, 'dashboard/index1.html', context)


def category(request):
	category = IndexCategory.objects.all()
	if request.method == 'POST':
		form = IndexCategoryForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('dashboard:category')
		else:
		    return redirect('dashboard:category')

	else:
		form = IndexCategoryForm()
	context = {'category':category, 'form':form}
	return render(request, 'dashboard/category.html', context)



@login_required(login_url='/account/login/')
def subcategory(request):
	if request.method == 'POST':

		name = request.POST.get('name')
		category = request.POST.get('category')
		unisex = request.POST.get('unisex')
		total_count = request.POST.get('total_count')
		try:
			category_qs = IndexCategory.objects.get(name=category, unisex=unisex)
			try:
				subcategory_qs = IndexSubCategory.objects.get(mycategory=category_qs, name=name)
				print("existed")
				return redirect('dashboard:subcategory')
			except IndexSubCategory.DoesNotExist:
				subcategory_qs =  IndexSubCategory.objects.create(mycategory=category_qs, name=name, total_count=total_count)
				print("doesnt exist")
				return redirect('dashboard:subcategory')
		except IndexCategory.DoesNotExist:
			return redirect('dashboard:subcategory')
	qs = IndexSubCategory.objects.all()
	category = set(IndexCategory.objects.values_list('name', flat=True))
	unisex =  ["Men", "Women", "Boys", "Girls"]
	return render(request, 'dashboard/subcategory.html', {'qs':qs,'category':category, 'unisex':unisex})

def deletesubcategory(request, id):
    qs = IndexSubCategory.objects.get(id=id)
    qs.delete()
    return redirect('dashboard:subcategory')

def deletecategory(request, id):
    qs = IndexCategory.objects.get(id=id)
    qs.delete()
    return redirect('dashboard:category')

def ordered_delivery(request):
	qs = Order.objects.filter(delivered=False, paid=False)
	context = {'qs':qs}
	return render(request, 'dashboard/ordered_delivery.html', context)

def order_delivery_details(request, id):
	order = get_object_or_404(Order, id=id)
	total_price = 0
	total_count = 0
	qs = order.order_name.all()
	for i in qs:
		total_price = total_price + i.total_price
		total_count = total_count + i.quantity
	context = {'qs':qs, 'total_count':total_count, 'total_price':total_price}
	return render(request, 'dashboard/order_delivery_details.html', context)

def order_pending_delivery_change(request, id):
	order = get_object_or_404(Order, id=id)
	cart = Cart.objects.filter(order_key = order)
	if order.paid == True:
		order.paid = False
		order.delivered = False
		order.save()
		for i in cart:
			i.paid=False
			i.save()

	elif order.paid == False:
		order.paid = True
		order.delivered = True
		order.save()
		for i in cart:
			i.paid=True
			i.save()
	return redirect('dashboard:ordered_delivery')

def order_delivered_change(request, id):
	order = get_object_or_404(Order, id=id)
	cart = Cart.objects.filter(order_key = order)
	if order.paid == True:
		order.paid = False
		order.delivered = False
		order.save()
		for i in cart:
			i.paid=False
			i.save()

	elif order.paid == False:
		order.paid = True
		order.delivered = True
		order.save()
		for i in cart:
			i.paid=True
			i.save()
	return redirect('dashboard:todaysreportorder')


@login_required(login_url='/account/login/')
def todaysreportorder(request):
    today = date.today()
    qs = Order.objects.filter(delivered=True, paid=True, date=today)
    context = {'qs':qs} #'Trouser':Trouser, 'TrouserPrice':TrouserPrice, 'ShortsPrice':ShortsPrice, 'TShirtsPrice':TShirtsPrice, 'ShoePrice':ShoePrice,'UnderwearPrice':UnderwearPrice, 'BoxerPrice':BoxerPrice,'SingletPrice':SingletPrice, 'PantPrice':PantPrice, 'SocksPrice':SocksPrice}
    return render(request, 'dashboard/todaysreportorder.html', context)

@login_required(login_url='/account/login/')
def todaysreportsold(request):
	today = date.today()
	total_price = 0
	total_count = 0
	qs = Cart.objects.filter(paid=True, date=today)
	for i in qs:
		total_price = total_price + i.total_price
		total_count = total_count + i.quantity

	context = {'qs':qs, 'total_price':total_price, 'total_count':total_count}
	return render(request, 'dashboard/todaysreportsold.html', context)

def filter_items(request, unisex, categoryid, subcategoryid, size):
	category = get_object_or_404(IndexCategory, id=categoryid, unisex__iexact=unisex)
	subcategory = get_object_or_404(IndexSubCategory, id=subcategoryid)
	qs = Index.objects.filter(category=category, subcategory=subcategory, size__iexact=size)
	total_count = qs.count()
	if request.method == 'POST':
		form = IndexForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			if unisex == 'Men' or unisex == 'men' or unisex == 'Boys' or unisex == 'boys':
				sex = 'M'
			elif unisex == "Women" or unisex == 'women' or unisex == 'girls' or unisex == 'girls':
				sex = "F"
			qs = form.save(commit=False)
			qs.category = category
			qs.subcategory = subcategory
			qs.sex = sex
			qs.size = size
			qs.price =1000
			qs.save()
			return redirect('dashboard:filter_items', unisex, categoryid, subcategoryid, size)
	else:
		form = IndexForm()
	context = {'qs':qs, 'category':category, 'subcategory':subcategory, 'total_count':total_count, 'unisex':unisex, 'size':size, 'categoryid':categoryid, 'subcategoryid':subcategoryid, 'form':form}
	return render(request, 'dashboard/filter_index.html', context)

def delete_items(request, unisex, categoryid, subcategoryid, size, id):
	qs = get_object_or_404(Index, id=id)
	qs.delete()
	return redirect('dashboard:filter_items', unisex, categoryid, subcategoryid, size)

