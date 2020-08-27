from django.shortcuts import render, get_object_or_404, redirect
from index.models import Index, IndexSize, IndexCategory, IndexSubCategory
from django.http import HttpResponse, JsonResponse
from cart.models import Cart
from order.models import Order
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from datetime import datetime, timedelta, date
from .forms import IndexForm, IndexCategoryForm, IndexSubCategoryForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from order.models import Order
import string
import random
from project.utils import render_to_pdf
from django.template.loader import get_template
from django.utils import timezone
import barcode
from barcode.writer import ImageWriter


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def dashboard(request):
	if request.user.username == 'cashier':
		return redirect('administrator:products')
	elif request.user.username == 'cashier02':
		return redirect('administrator:products')
	totalitems = Index.objects.all()
	category = IndexCategory.objects.all()
	subcategory = IndexSubCategory.objects.all()
	context = {'subcategory':subcategory, 'category':category, 'totalitems':totalitems}
	return render(request, 'dashboard/index1.html', context)

@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def search_order_id(request):
    order_id = request.POST.get('order_id')
    qs = Order.objects.filter(order_id=order_id)
    return render(request, 'dashboard/search_order_id.html', {'qs':qs})


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def additem(request, id):
    total_add = request.POST.get('total_add')
    qs = Index.objects.get(id= int(id))
    qs.stock= qs.stock + int(total_add)
    qs.save()
    cat_id = qs.category.id
    sub_cat_id = qs.subcategory.id
    category = IndexCategory.objects.get(id=cat_id)
    subcategory = IndexSubCategory.objects.get(id=sub_cat_id)
    category.total_count = category.total_count + int(total_add)
    category.save()
    subcategory.total_count = subcategory.total_count + int(total_add)
    subcategory.save()
    return JsonResponse({'response':'done'})


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def category(request):
	category = IndexCategory.objects.all()
	if request.method == 'POST':
		form = IndexCategoryForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('dashboard:category')
	else:
		form = IndexCategoryForm()
	context = {'category':category, 'form':form}
	return render(request, 'dashboard/category.html', context)



@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def subcategory(request):
	if request.method == 'POST':
		form = IndexSubCategoryForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('dashboard:subcategory')
	else:
		form = IndexSubCategoryForm()
	qs = IndexSubCategory.objects.all()
	return render(request, 'dashboard/subcategory.html', {'qs':qs,'form':form})


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def deletesubcategory(request, id):
    qs = IndexSubCategory.objects.get(id=id)
    qs.delete()
    return redirect('dashboard:subcategory')


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def deletecategory(request, id):
    qs = IndexCategory.objects.get(id=id)
    qs.delete()
    return redirect('dashboard:category')


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def ordered_delivery(request):
	qs = Order.objects.filter(delivered=False).order_by('-date', '-time')
	context = {'qs':qs}
	return render(request, 'dashboard/ordered_delivery.html', context)

@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def delete_order(request, id):
    qs = Order.objects.get(id=id)
    qs.delete()
    return redirect('dashboard:ordered_delivery')

@login_required(login_url='/account/login_dashboard/')
@staff_member_required
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


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def order_pending_delivery_change(request, id):
	order = get_object_or_404(Order, id=id)
	cart = Cart.objects.filter(order_key = order)
	if order.delivered == False:
		order.paid = True
		order.delivered = True
		order.save()
		for i in cart:
			i.paid=True
			i.save()
			category = i.product.category
			category.total_count = category.total_count - i.quantity
			category.save()
			subcategory = i.product.subcategory
			subcategory.total_count = subcategory.total_count - i.quantity
			subcategory.save()
			stock_available = i.product
			stock_available.stock = stock_available.stock - i.quantity
			stock_available.save()
	return redirect('dashboard:ordered_delivery')

@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def order_delivered_change(request, id):
	order = get_object_or_404(Order, id=id)
	cart = Cart.objects.filter(order_key = order)
	if order.delivered == False:
		order.paid = True
		order.delivered = True
		order.save()
		for i in cart:
			i.paid=True
			i.save()
	return redirect('dashboard:todaysreportorder')


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def todaysreportorder(request):
	today = date.today()
	order = Order.objects.filter(delivered=True, paid=True, date=today).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(order, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs}
	return render(request, 'dashboard/todaysreportorder.html', context)



@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def filter_items(request, categoryid, subcategoryid, sex, size):
	category = get_object_or_404(IndexCategory, id=categoryid)
	subcategory = get_object_or_404(IndexSubCategory, id=subcategoryid)
	qs = Index.objects.filter(category=category, subcategory=subcategory, sex=sex, size=size)
	total_count = qs.count()
	total_items = 0
	for i in qs:
	    total_items = total_items + i.stock

	if request.method == 'POST':
		form = IndexForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			try:
				name = form.cleaned_data['name']
				color = form.cleaned_data['color']
				filter = Index.objects.get(category=category, subcategory=subcategory, name=name, color=color, size=size, sex=sex)
				messages.info(request,'Records already exist please add another')
				return redirect('dashboard:filter_items', categoryid, subcategoryid, sex, size)
			except Index.DoesNotExist:
				qs = form.save(commit=False)
				qs.category = category
				qs.subcategory = subcategory
				qs.sex = sex
				qs.size = size
				qs.price = 1000
				qs.save()
				stock = form.cleaned_data['stock']
				category1 = IndexCategory.objects.get(id=categoryid)
				category1.total_count = category1.total_count + int(stock)
				category1.save()
				subcategory = get_object_or_404(IndexSubCategory, id=subcategoryid)
				subcategory.total_count = subcategory.total_count + int(stock)
				subcategory.save()
				return redirect('dashboard:filter_items', categoryid, subcategoryid, sex, size)

	else:
		form = IndexForm()
	context = {'qs':qs, 'category':category, 'subcategory':subcategory, 'total_count':total_count,
	 'categoryid':categoryid, 'subcategoryid':subcategoryid,'sex':sex,'size':size, 'form':form,'total_items':total_items}
	return render(request, 'dashboard/filter_index.html', context)


@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def delete_items(request, categoryid, subcategoryid,sex, id, size):
	qs = get_object_or_404(Index, id=id)
	qs.delete()
	return redirect('dashboard:filter_items', categoryid, subcategoryid, sex, size)


def filter_sold(request):
	if request.method == 'POST':
		date = request.POST.get('date')
		request.session['date'] = date

	elif not request.method == 'POST':
		try:
			date =  request.session['date']
		except KeyError:
			return HttpResponse('input date')
	total = 0
	amount = 0
	cart = Cart.objects.filter(paid=True, date=str(date)).order_by('-date')
	for i in cart:
		total = total + i.quantity
		amount = amount + i.total_price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'total':total, 'amount':amount}
	return render(request, 'dashboard/filter_sold.html', context)

@login_required(login_url='/account/login_dashboard/')
@staff_member_required
def todaysreportsold(request):
	today = date.today()
	total = 0
	amount = 0
	cart = Cart.objects.filter(paid=True, date=today).order_by('-date')
	for i in cart:
		total = total + i.quantity
		amount = amount + i.total_price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'total':total, 'amount':amount}
	return render(request, 'dashboard/todaysreportsold.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def weeklyreportorder(request):
	one_week_ago = datetime.today() - timedelta(days=7)
	order = Order.objects.filter(delivered=True, paid=True, date__gte=one_week_ago).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(order, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs}
	return render(request, 'dashboard/weeklyreportorder.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def weeklyreportsold(request):
	one_week_ago = datetime.today() - timedelta(days=7)
	total = 0
	amount = 0
	cart = Cart.objects.filter(paid=True, date__gte=one_week_ago).order_by('-date')
	for i in cart:
		total = total + i.quantity
		amount = amount + i.total_price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'total':total, 'amount':amount}
	return render(request, 'dashboard/weeklyreportsold.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def monthlyreportorder(request):
	order = Order.objects.filter(delivered=True, paid=True, date__month__gte=1).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(order, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs}
	return render(request, 'dashboard/monthlyreportorder.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def monthlyreportsold(request):
	total = 0
	amount = 0
	cart = Cart.objects.filter(paid=True, date__month__gte=1).order_by('-date')
	for i in cart:
		total = total + i.quantity
		amount = amount + i.total_price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'total':total, 'amount':amount}
	return render(request, 'dashboard/monthlyreportsold.html', context)



@login_required(login_url='/account/login/')
@staff_member_required
def yearlyreportorder(request):
	order = Order.objects.filter(delivered=True, paid=True, date__year__gte=2019).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(order, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs}
	return render(request, 'dashboard/yearlyreportorder.html', context)

@login_required(login_url='/account/login/')
@staff_member_required
def yearlyreportsold(request):
	total = 0
	amount = 0
	cart = Cart.objects.filter(paid=True, date__year__gte=2019).order_by('-date')
	for i in cart:
		total = total + i.quantity
		amount = amount + i.total_price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'total':total, 'amount':amount}
	return render(request, 'dashboard/yearlyreportsold.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def pay(request, id):
	sum = 0
	paymentoption = request.POST.get('paymentoption')
	date=datetime.now()
	num = random.randrange(12345678910234)
	num = str(num)
	if len(str(num)) == 11:
	    num = str(num) + 1
	    num = int(num)
	else:
	    num = num

	ean = barcode.get('ean13', str(num), writer=ImageWriter())
	filename = ean.save('ean13')
	file = open('/home/budescode/inventory/project/static/images/barcode.png', 'wb')
	ean.write(file)
	total_price = 0
	total_qty = 0
	order = get_object_or_404(Order, id=id, paid=True)
	orderitems = Cart.objects.filter(order_key=order)
	for i in orderitems:
	    total_price = total_price + i.total_price
	    total_qty = total_qty + i.quantity


	template = get_template('dashboard/printreceipt')
	context={'orderitems':orderitems, 'order':order, 'total_price':total_price, 'date':date,  'user': request.user.username, 'total_qty':total_qty}
	#return render (request, 'Administrator/order.html', context)
	html = template.render(context)
	pdf = render_to_pdf('dashboard/printreceipt', context)
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
