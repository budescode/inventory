from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
import csv, io
from django.contrib import messages
from .models import Category, SubCategory, MyItems, Cart, Image, PettyCash
from project.utils import render_to_pdf
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime, timedelta, date
import barcode
from barcode.writer import ImageWriter
# from StringIO import StringIO
import string
import random
from django.db.models import Avg, Sum, Count
from .forms import PettyCashForm, SubCategoryForm
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required




@login_required(login_url='/account/login/')
@staff_member_required
def comparereport(request):
    return render(request, 'Administrator/comparereport1.html')




@login_required(login_url='/account/login/')
@staff_member_required
def weeklyreport(request):
	one_week_ago = datetime.today() - timedelta(days=7) # filter by 1 week
	cart = Cart.objects.filter(date__gte=one_week_ago, paid=True)
	carttotal = 0
	cartprice = 0
	for i in cart:
		carttotal = carttotal + i.qty
		cartprice = cartprice + i.price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'carttotal':carttotal, 'cartprice':cartprice}
	return render(request, 'Administrator/weeklyreport.html', context)



@login_required(login_url='/account/login/')
@staff_member_required
def monthlyreport(request):
	cart = Cart.objects.filter(paid=True, date__month__gte=1)
	carttotal = 0
	cartprice = 0
	for i in cart:
		carttotal = carttotal + i.qty
		cartprice = cartprice + i.price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'carttotal':carttotal, 'cartprice':cartprice}
	return render(request, 'Administrator/monthlyreport.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def yearlyreport(request):
	cart = Cart.objects.filter(paid=True, date__year__gte=2019)
	carttotal  = 0
	cartprice = 0
	for i in cart:
		carttotal = carttotal + i.qty
		cartprice = cartprice + i.price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'carttotal':carttotal, 'cartprice':cartprice}
	return render(request, 'Administrator/yearlyreport.html', context)


@login_required(login_url='/account/login/')
def todaysreport(request):
    cart = Cart.objects.filter(date=timezone.now(), paid=True)
    carttotal = 0
    cartprice = 0
    for i in cart:
        carttotal = carttotal + i.qty
        cartprice = cartprice + i.price
    context = {'carttotal':carttotal, 'cart':cart, 'cartprice':cartprice}
    return render(request, 'Administrator/todaysreport.html', context)



@login_required(login_url='/account/login/')
@staff_member_required
def home(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    else:
	    return render(request, 'Administrator/index.html')


@login_required(login_url='/account/login/')
@staff_member_required
def dailyReportView(request):
	total_price = 0
	total_cart = 0
	date = datetime.now()
	cart1 = Cart.objects.filter(date=datetime.now(), paid=True)
	for i in cart1:
		total_price = total_price+i.price
		total_cart = total_cart + i.qty
	subject = "Daily Sales"
	from_email = settings.EMAIL_HOST_USER
	# Now we get the list of emails in a list form.
	to_email = ['accountant@yehgs.co.uk']
	#Opening a file in python, with closes the file when its done running
	with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
	    sign_up_message = sign_up_email_txt_file.read()
	message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
	html_template = get_template("Administrator/dailyreport.html").render({'qs':cart1, 'total_cart':total_cart, 'total_price':total_price, 'date':date})
	message.attach_alternative(html_template, "text/html")
	message.send()
	return render(request, 'Administrator/dailyreportsuccess.html', context={'total_price':total_price})

@staff_member_required
def filter_index(request):
    sex = request.POST.get('sex')
    size = request.POST.get('size')
    category = request.POST.get('category')
    subcategory = request.POST.get('subcategory')
    return render (request, 'index_filter.html')


# Create your views here.
@login_required(login_url='/account/login/')
@staff_member_required
def administrator(request):
	if request.user.username == 'cashier':
	    return redirect('administrator:products')
	elif request.user.username == 'cashier02':
	    return redirect('administrator:products')
	totalitems = MyItems.objects.all()
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	context = {'subcategory':subcategory, 'category':category, 'totalitems':totalitems}
	return render(request, 'Administrator/index1.html', context)




@login_required(login_url='/account/login/')
@staff_member_required
def category(request):
    qs = Category.objects.all()
    return render(request, 'Administrator/category.html', {'qs':qs})

@login_required(login_url='/account/login/')
@staff_member_required
def subcategory(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('administrator:subcategory')
    else:
        form = SubCategoryForm()
    qs = SubCategory.objects.all()
    return render(request, 'Administrator/subcategory.html', {'qs':qs, 'form':form})


@login_required(login_url='/account/login/')
@staff_member_required
def deletecategory(request, id):
    qs = Category.objects.get(id=id)
    qs.delete()
    return redirect('administrator:category')


@login_required(login_url='/account/login/')
@staff_member_required
def deletesubcategory(request, id):
    qs = SubCategory.objects.get(id=id)
    qs.delete()
    return redirect('administrator:subcategory')


@login_required(login_url='/account/login/')
@staff_member_required
def addtoCategory(request):
	category = request.POST.get("category")
	stock = request.POST.get("stock")
	qs = Category.objects.create(name=category, total_count=int(stock))
	return JsonResponse({"category":category})

@login_required(login_url='/account/login/')
@staff_member_required
def addSubCategory(request):
	subcategory = request.POST.get("subcategory")
	qs = SubCategory.objects.create(name=subcategory)
	return JsonResponse({"subcategory":subcategory})


@login_required(login_url='/account/login/')
@staff_member_required
def userpostsview(request):
	qs = MyItems.objects.all().order_by('category')
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	cart = Cart.objects.filter(user=request.user, paid=False)
	context = {"qs":qs, 'category':category, 'subcategory':subcategory, 'cart':cart}
	return render(request, 'Administrator/products.html', context)


@login_required(login_url='/account/login/')
@staff_member_required
def editmyitems(request):
	editcategoryid = request.POST.get('editcategoryid')
	editsubcategoryid = request.POST.get('editsubcategoryid')
	editsex = request.POST.get('editsex')
	editsize = request.POST.get('editsize')
	if editsize == 'XL2':
		editsize = '2XL'
	elif editsize == 'XL3':
		editsize = '3XL'
	elif editsize == 'XL4':
		editsize = '4XL'
	else:
		editsize = editsize
	editstock = request.POST.get('editstock')
	category = Category.objects.get(id=int(editcategoryid))
	subcategory = SubCategory.objects.get(id=int(editsubcategoryid))
	try:
		qs = MyItems.objects.get(category=category, subcategory=subcategory, sex=editsex, size = editsize)
		qs.stock = qs.stock + int(editstock)
		qs.save()
		category.total_count = category.total_count + int(editstock)
		subcategory.total_count = subcategory.total_count + int(editstock)
		category.save()
		subcategory.save()
	except MyItems.DoesNotExist:
		qs = MyItems.objects.create(category=category, subcategory=subcategory, sex=editsex, size = editsize, stock=int(editstock), price=1000)
		category.total_count = category.total_count + int(editstock)
		subcategory.total_count = subcategory.total_count + int(editstock)
		category.save()
		subcategory.save()

	return JsonResponse({'editcategoryid':editcategoryid, 'editsubcategoryid':editsubcategoryid, 'editsex':editsex, 'editsize':editsize })


#this function is to edit categories
@login_required(login_url='/account/login/')
@staff_member_required
def editmycategory(request):
	editcategoryid = request.POST.get('editcategoryid')
	edittotal = request.POST.get('edittotal')
	category = Category.objects.get(id=int(editcategoryid))
	category.total_count = int(edittotal)
	category.save()
	return JsonResponse({'editcategoryid':editcategoryid, 'edittotal':edittotal})


#this function is to edit subcategories
@login_required(login_url='/account/login/')
@staff_member_required
def editmysubcategory(request):
	editsubcategoryid = request.POST.get('editsubcategoryid')
	edittotal = request.POST.get('edittotal')
	subcategory = SubCategory.objects.get(id=int(editsubcategoryid))
	subcategory.total_count = int(edittotal)
	subcategory.save()
	return JsonResponse({'editsubcategoryid':editsubcategoryid, 'edittotal':edittotal})

@login_required(login_url='/account/login/')
@staff_member_required
def addCart(request):
    cat_id = int(request.POST.get('cat_id'))
    subcat_id = int(request.POST.get('subcat_id'))
    qty = int(request.POST.get('qty'))
    category = Category.objects.filter(id=cat_id)
    if not category.exists():
        return JsonResponse({"error":'category doesnt exist'})
    subcategory = SubCategory.objects.filter(id=subcat_id)
    if not subcategory.exists():
        return JsonResponse({"error":'subcategory doesnt exist'})
    try:
        category = Category.objects.get(id=cat_id)
        subcategory = SubCategory.objects.get(id=subcat_id)
        sex = request.POST.get('sex')
        size = request.POST.get('size')
        qs = MyItems.objects.get(sex=sex, category=category, subcategory=subcategory, size=size)
        Cart.objects.create(user = request.user, category=category, size=size, subcategory=subcategory,  sex=sex, qty=qty, price= 1000 * qty, single_price=1000, date=timezone.now(), product_id=qs.id)
        report =  "Record Created"
        total = 0
        a = 0
        for i in Cart.objects.filter(paid=False, user=request.user).all():
            total = total + i.qty
            a = a+i.price
        return JsonResponse({"cart_total":total, 'id':qs.id, 'total_price':a, 'category':category.name, 'subcategory':subcategory.name, 'qty':qty})
    except MyItems.DoesNotExist:
        report = 'No Records found'
        return JsonResponse({'report':report})




@login_required(login_url='/account/login/')
@staff_member_required
def addtoCart(request):
	post_pk = request.POST.get("post_pk")
	qty1 = request.POST.get("qty")
	qty = int(qty1)
	category1 = request.POST.get('category')
	category = Category.objects.get(name=category1)
	subcategory1 = request.POST.get('subcategory')
	subcategory = SubCategory.objects.get(name = subcategory1, mycategory=category)
	sex = request.POST.get('sex')
	size = request.POST.get('size')
	try:
	    qs = MyItems.objects.get(sex=sex, category=category, subcategory=subcategory, size=size)
	    Cart.objects.create(user = request.user, category=category, size=size, subcategory=subcategory,  sex=sex, qty=qty, price= 1000 * qty, single_price=1000, date=timezone.now(), product_id=qs.id)
	    report =  "Record Created"
	    total = 0
	    a = 0
	    for i in Cart.objects.filter(paid=False, user=request.user).all():
	        total = total + i.qty
	        a = a+i.price
	    return JsonResponse({"cart_total":total, 'id':post_pk, 'total_price':a, 'qty':qty, 'category':category.name, 'subcategory':subcategory.name})
	except MyItems.DoesNotExist:
	    report = 'No Records found'
	    return JsonResponse({'report':report, 'id':post_pk,})


@login_required(login_url='/account/login/')
@staff_member_required
def editCart(request):
	post_pk = request.POST.get("post_pk")
	post_pk = int(post_pk)
	qty1 = request.POST.get("qty")
	qty1 = int(qty1)
	itemid = request.POST.get("id")
	itemid = int(itemid)
	qty = int(qty1)
	#update old details
	qs = Cart.objects.get(product_id = post_pk, id=itemid, paid=False)
	qs.price = qs.single_price * qty
	qs.qty = qty
	qs.save()
	qs = Cart.objects.get(product_id = post_pk, id=itemid, paid=False)
	total_price1 = Cart.objects.filter(paid=False, user=request.user)
	a = 0
	b = 0
	for i in total_price1:
		a = a+i.price
		b = b + i.qty
	return JsonResponse({"cart_total":b, 'id':itemid, 'total_price':a, 'qty':qty, 'price':qs.price, 'single_price':qs.single_price})

@login_required(login_url='/account/login/')
@staff_member_required
def deleteCart(request, id, product_id):
	qs = Cart.objects.get(id=id)
	qs.delete()
	return redirect('administrator:cart')
	#return JsonResponse({"cart_total":cart, 'id':post_pk, 'total_price':a})

@login_required(login_url='/account/login/')
@staff_member_required
def cart(request):
	qs = Cart.objects.filter(paid=False, user=request.user)
	return render(request, 'Administrator/cart.html', {"qs":qs})


@login_required(login_url='/account/login/')
@staff_member_required
def mysales(request):
	qs = Cart.objects.filter(paid=True).order_by('-date')
	return render(request, 'Administrator/mysales.html', {"qs":qs})


@login_required(login_url='/account/login/')
@staff_member_required
def additems(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    category = request.POST.get("category")
    category = Category.objects.get(name=category)
    subcategory = request.POST.get("subcategory")

    try:
        sub = SubCategory.objects.get(name=subcategory, mycategory=category)
    except SubCategory.DoesNotExist:
        return JsonResponse({'error':'Category and subcategory mismatch'})

    sex = request.POST.get("sex")
    size = request.POST.get("size")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    qs = MyItems.objects.filter(category=category, subcategory=sub, sex=sex, price=price,size=size)

    if qs.exists():
        for i in qs:
            i.stock = stock
            i.save()
            sub.total_count = int(sub.total_count) + int(stock)
            category.total_count = int(category.total_count) + int(stock)
            sub.save()
            category.save()

            return JsonResponse({"category":str(category.name), 'sex':sex, 'price':price, 'stock':stock, 'error':'none'})

    else:
        newitem = MyItems.objects.create(category=category, subcategory=sub, sex=sex, price=price, stock=stock, size=size)
        newitem.save()
        sub.total_count = int(sub.total_count) + int(stock)
        category.total_count = int(category.total_count) + int(stock)
        sub.save()
        category.save()
        return JsonResponse({"category":str(category.name), 'sex':sex, 'price':price, 'stock':stock, 'product_id':newitem.id, 'error':'none'})


@login_required(login_url='/account/login/')
@staff_member_required
def editItems(request):
	if request.user.username == 'cashier':
		return redirect('administrator:products')
	stock = request.POST.get("stock")
	product_id = request.POST.get("product_id")
	myitems = MyItems.objects.get(pk=int(product_id))
	myitems.stock = int(myitems.stock) + int(stock)
	myitems.save()
	return JsonResponse({'stock':myitems.stock, 'product_id':product_id})


@login_required(login_url='/account/login/')
@staff_member_required
def deletemyItems(request):
	product_id = request.POST.get('product_id')
	item = MyItems.objects.get(id=product_id)
	item.delete()
	return JsonResponse({'product_id':product_id})



@login_required(login_url='/account/login/')
@staff_member_required
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


@login_required(login_url='/account/login/')
@staff_member_required
def pettyCash(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs=PettyCash.objects.all()
    return render(request, 'Administrator/pettycash.html', {'qs':qs})

@login_required(login_url='/account/login/')
@staff_member_required
def addpettyCash(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    if request.method == 'POST':
        form = PettyCashForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('administrator:pettycash')
    else:
        form = PettyCashForm(request.POST or None)
    context = {"form": form}
    return render(request, "Administrator/addpettycash.html", context)

@login_required(login_url='/account/login/')
@staff_member_required
def delete_pettycash(request, id):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs = PettyCash.objects.get(id=id)
    qs.delete()
    return redirect('administrator:pettycash')

@login_required(login_url='/account/login/')
@staff_member_required
def edit_pettycash(request, id):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs = PettyCash.objects.get(id=id)
    #if request.method == 'POST':
    form = PettyCashForm(request.POST or None, request.FILES or None, instance=qs)
    if form.is_valid():

        sex = form.cleaned_data.get('sex')
        price = form.cleaned_data.get('price')
        qs.sex = sex
        qs.price = price
        qs.save()

        return redirect('administrator:pettycash')
    #else:
        #form = ProfileForm(request.POST or None, instance=qs)
    context = {"form": form}
    return render(request, "administrator/editpettycash.html", context)

@login_required(login_url='/account/login/')
@staff_member_required
def deleteAllCart(request):
    qs = Cart.objects.filter(paid=False)
    for i in qs:
        i.paid=True
        i.save()
    return redirect('administrator:products')



@login_required(login_url='/account/login/')
@staff_member_required
def pay(request):
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
	qs = Cart.objects.filter(paid=False, user=request.user)
	total_cart = Cart.objects.filter(paid=False, user=request.user).count()
	total_price = 0
	#image = Image.objects.get(id=1)
	qs1 = []
	order_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
	order_id = str(order_id)
	for i in qs:
		total_price = total_price + (i.price)
		i.paid = True
		i.product_id = order_id
		qs1.append(i)
		i.paymentoption = paymentoption
		cate = i.category
		subcate = i.subcategory
		cate.total_count = cate.total_count -  i.qty
		cate.save()
		subcate.total_count = subcate.total_count -  i.qty
		subcate.save()
		items = MyItems.objects.get(category=cate, subcategory=subcate, size = i.size, sex = i.sex)
		items.stock = items.stock - i.qty
		items.save()
		i.save()

	template = get_template('Administrator/order.html')
	context={'qs':qs1, 'total_cart':total_cart, 'total_price':total_price, 'date':date, 'paymentoption':paymentoption, 'order_id':order_id, 'user': request.user.username}
	#return render (request, 'Administrator/order.html', context)
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

@login_required(login_url='/account/login/')
@staff_member_required
def filtersales(request):
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
		total = total + i.qty
		amount = amount + i.price
	page = request.GET.get('page', 1)
	paginator = Paginator(cart, 80)
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {'qs':qs, 'total':total, 'amount':amount}
	return render(request, 'Administrator/filtersales.html', context)
