from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from index.models import Poster
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
import csv, io
from django.contrib import messages
from .models import Category, MyItems, Cart, Image, PettyCash
from project.utils import render_to_pdf
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
# from StringIO import StringIO
import random
from django.db.models import Avg, Sum, Count
from .forms import PettyCashForm
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives





@login_required(login_url='/account/login/')
def home(request):

    if request.user.username == 'cashier':
        return redirect('administrator:products')

    else:
	    return render(request, 'Administrator/index1.html')



def dailyReportView(request):
	total_price = 0
	date = datetime.now()
	cart1 = Cart.objects.filter(date=datetime.now(), paid=True)
	total_cart = Cart.objects.filter(date=datetime.now(), paid=True).count()
	for i in cart1:
		total_price = total_price+i.price

	subject = "Daily Sales"
	from_email = settings.EMAIL_HOST_USER
	# Now we get the list of emails in a list form.
	to_email = ['aceplayhousehq@gmail.com']
	#Opening a file in python, with closes the file when its done running
# 	detail2 = "http://budescode.pythonanywhere.com/account/"+ str(test.user_id) + '/' + username
	with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
	    sign_up_message = sign_up_email_txt_file.read()
	message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
	html_template = get_template("Administrator/dailyreport.html").render({'qs':cart1, 'total_cart':total_cart, 'total_price':total_price, 'date':date})
	message.attach_alternative(html_template, "text/html")
	message.send()
	return render(request, 'Administrator/dailyreportsuccess.html')

# Create your views here.
@login_required(login_url='/account/login/')
def administrator(request):

	# print('time', datetime.today().strftime('%Y-%m-%d'))
	if request.user.username == 'cashier':
	    return redirect('administrator:products')
	totalitems = MyItems.objects.all()
	date = datetime.now()
	cart = Cart.objects.filter(date=datetime.now())


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
	category = Category.objects.all()
	context = {'category':category, 'sales_Socks_total':sales_Socks_total,'sales_Pant_total':sales_Pant_total,'sales_Boxer_total':sales_Boxer_total,'sales_Singlet_total':sales_Singlet_total,'sales_Underwear_total':sales_Underwear_total,'Sales_Shoe_total':Sales_Shoe_total,'Sales_T_Shirts_total':Sales_T_Shirts_total ,'Shorts_total':Shorts_total ,'Sales_Trouser_total':Sales_Trouser_total, 'totalitems':totalitems, 'Socks_total':Socks_total, 'Socks_percentage':Socks_percentage,'Pant_total':Pant_total, 'Pant_percentage':Pant_percentage, 'Boxer_total':Boxer_total, 'Boxer_percentage':Boxer_percentage, 'Singlet_total':Singlet_total, 'Singlet_percentage':Singlet_percentage, 'Underwear_total':Underwear_total, 'Underwear_percentage':Underwear_percentage, 'Shoe_total':Shoe_total, 'Shoe_percentage':Shoe_percentage, 'T_Shirts_total':T_Shirts_total, 'T_Shirts_percentage':T_Shirts_percentage, 'Trouser_percentage':Trouser_percentage,'Trouser_total':Trouser_total, 'Trouser_percentage':Trouser_percentage, 'Shorts_total':Shorts_total, 'Shorts_percentage':Shorts_percentage}
	return render(request, 'Administrator/index.html', context)




@login_required(login_url='/account/login/')
def category(request):
    qs = Category.objects.all()
    return render(request, 'Administrator/category.html', {'qs':qs})



def addtoCategory(request):
	category = request.POST.get("category")
	qs = Category.objects.create(name=category)
	return JsonResponse({"category":category})





# @login_required(login_url='/account/login/')
@login_required(login_url='/account/login/')
def userpostsview(request):
	qs = MyItems.objects.all()
	context = {"qs":qs}
	return render(request, 'Administrator/products.html', context)


def addtoCart(request):
	post_pk = request.POST.get("post_pk")
	qty1 = request.POST.get("qty")
	qty = int(qty1)
	qs = MyItems.objects.get(pk=post_pk)
	qs.stock = qs.stock-qty
	qs.save()
	Cart.objects.create(category=qs.category, description=qs.description, qty=qty, price=qs.price*qty, single_price=qs.price, date=timezone.now(), product_id=post_pk)

	cart = Cart.objects.filter(paid=False).count()
	total_price1 = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price1:
		a = a+i.price
	return JsonResponse({"cart_total":cart, 'id':post_pk, 'total_price':a, 'qty':qty, 'qs':qs.stock})


def editCart(request):
	post_pk = request.POST.get("post_pk")
	post_pk = int(post_pk)
	qty1 = request.POST.get("qty")
	qty1 = int(qty1)
	itemid = request.POST.get("id")
	itemid = int(itemid)

	print('tttttt', post_pk, qty1)
	qty = int(qty1)
	qs = Cart.objects.get(product_id = post_pk, id=itemid, paid=False)
	qs.price = qs.single_price * qty
	qs1 = MyItems.objects.get(pk=post_pk)
	print('old stock', qs1.stock)
	qs1.stock = qs1.stock - qs.qty
	qs1.save()
	print('removed stock', qs1.stock)

	qs.qty = qty
	qs.save()

	qs = Cart.objects.get(product_id = post_pk, id=itemid, paid=False)
	qs1.stock = qs1.stock + qty
	qs1.save()
	print('new stock', qs1.stock)


	cart = Cart.objects.filter(paid=False).count()
	total_price1 = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price1:
		a = a+i.price
	print(qs.single_price)
	return JsonResponse({"cart_total":cart, 'id':itemid, 'total_price':a, 'qty':qty, 'price':qs.price, 'single_price':qs.single_price})

def deleteCart(request, id, product_id):

	#post_pk = request.POST.get("post_pk")
	qs = Cart.objects.get(id=id)
	qs1 = MyItems.objects.get(id=product_id)
	qs1.stock = qs1.stock + qs.qty
	qs1.save()
	qs.delete()
	return redirect('administrator:cart')
	#return JsonResponse({"cart_total":cart, 'id':post_pk, 'total_price':a})


def cart(request):
	qs = Cart.objects.filter(paid=False)
	return render(request, 'Administrator/cart.html', {"qs":qs})

def mysales(request):
	qs = Cart.objects.filter(paid=True).order_by('-date')
	return render(request, 'Administrator/mysales.html', {"qs":qs})

def viewDetails(request):
	post_pk = request.POST.get("post_pk")
	post = Poster.objects.get(id_user=post_pk)
	data = serializers.serialize('json', [post])
	return JsonResponse({"data":data})

def additems(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    category = request.POST.get("category")
    description = request.POST.get("description")
    size = request.POST.get("size")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    newitem = MyItems.objects.create(category=category, description=description, price=price, stock=stock, size=size)
    newitem.save()
    return JsonResponse({"category":category, 'description':description, 'price':price, 'stock':stock, 'product_id':newitem.id})


def editItems(request):
	if request.user.username == 'cashier':
		return redirect('administrator:products')
	stock = request.POST.get("stock")
	product_id = request.POST.get("product_id")
	myitems = MyItems.objects.get(pk=int(product_id))
	myitems.stock = int(myitems.stock) + int(stock)
	myitems.save()
	return JsonResponse({'stock':myitems.stock, 'product_id':product_id})


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


def pettyCash(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs=PettyCash.objects.all()
    return render(request, 'Administrator/pettycash.html', {'qs':qs})

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

def delete_pettycash(request, id):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs = PettyCash.objects.get(id=id)
    qs.delete()
    return redirect('administrator:pettycash')

def edit_pettycash(request, id):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs = PettyCash.objects.get(id=id)
    #if request.method == 'POST':
    form = PettyCashForm(request.POST or None, request.FILES or None, instance=qs)
    if form.is_valid():

        description = form.cleaned_data.get('description')
        price = form.cleaned_data.get('price')
        qs.description = description
        qs.price = price
        qs.save()

        return redirect('administrator:pettycash')
    #else:
        #form = ProfileForm(request.POST or None, instance=qs)
    context = {"form": form}
    return render(request, "administrator/editpettycash.html", context)

def deleteAllCart(request):
    qs = Cart.objects.filter(paid=False)
    for i in qs:
        i.paid=True
        i.save()
    return redirect('administrator:products')




def pay(request):
	sum = 0
	date=datetime.now()
	num = random.randrange(12345678910234)
	ean = barcode.get('ean13', str(num), writer=ImageWriter())
	filename = ean.save('ean13')
	file = open('/home/budescode/inventory/project/static/images/barcode.png', 'wb')
	ean.write(file)
	qs = Cart.objects.filter(paid=False)
	total_cart = Cart.objects.filter(paid=False).count()
	total_price = 0
	image = Image.objects.get(id=1)
	for i in qs:
	    total_price = total_price + (i.price)
	template = get_template('Administrator/order.html')
	context={'qs':qs, 'total_cart':total_cart, 'total_price':total_price, 'date':date}
	#return render (request, 'Administrator/order.html', context)
	for i in qs:
	    i.paid = True
	    i.save()
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
def filtersales(request):
	date = request.POST.get('date')
	print(date)
	qs = Cart.objects.filter(paid=True, date=str(date)).order_by('-date')
	return render(request, 'Administrator/filtersales.html', {"qs":qs})
