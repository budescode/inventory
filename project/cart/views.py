from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from .models import Cart
from order.models import Order
from index.models import Index, IndexSize, IndexCategory, IndexSubCategory
import string
import random
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
import json

# @login_required(login_url='/account/login/')
def addtoCart(request):
	product_id = request.POST.get('product_id')
	size = request.POST.get('size')
	try:
		qs = Index.objects.get(id=int(product_id))
		detail = Index.objects.filter(category=qs.category,subcategory=qs.subcategory, name=qs.name, size=size, sex=qs.sex, color=qs.color)[0]
		if detail.stock == 0:
			return JsonResponse({'error':'Out Of Stock'})
		else:
			quantity = request.POST.get('quantity')
			total_price = 1000 * int(quantity)
			if request.user.is_authenticated:
			    Cart.objects.create(product=detail, size=size, sex=detail.sex, quantity=int(quantity), user=request.user, paid=False, unit_price=1000, total_price=total_price)
			    return JsonResponse({'response':'done'})
			else:
				try:
				    session_cart = request.session['session_cart']
				    length = len(session_cart)
				    length1 = length + 1
				    session_cart.append({'image':str(detail.image), 'id':str(detail.id), 'length':str(length1), 'size':size, 'sex':detail.sex, 'quantity': str(quantity), 'unit_price':'1000', 'total_price':str(total_price)})
				    request.session['session_cart'] = session_cart
				except KeyError:
				    request.session['session_cart'] = [{'image':str(detail.image), 'id':str(detail.id), 'length':'1', 'size':size, 'sex':detail.sex, 'quantity': str(quantity), 'unit_price':'1000', 'total_price':str(total_price)}]
				return JsonResponse({'response':'done'})

	except Index.DoesNotExist:
		return JsonResponse({'error':'Size Unavailable, please select other sizes'})
	except IndexError:
		return JsonResponse({'error':'Item Unavailable'})

def buynow(request):
	product_id = request.POST.get('product_id')
	size = request.POST.get('size')
	try:
		qs = Index.objects.get(id=int(product_id))
		detail = Index.objects.filter(category=qs.category,subcategory=qs.subcategory, name=qs.name, size=size, sex=qs.sex, color=qs.color )[0]
		if detail.stock == 0:
		    messages.info(request,'Out Of Stock')
		    return redirect('cart:viewCart')
		else:
			quantity = request.POST.get('quantity')
			total_price = 1000 * int(quantity)
			if request.user.is_authenticated:
			    Cart.objects.create(product=detail, size=size, sex=detail.sex, quantity=int(quantity), user=request.user, paid=False, unit_price=1000, total_price=total_price)
			    return redirect('cart:viewCart')
			else:
				try:
				    session_cart = request.session['session_cart']
				    length = len(session_cart)
				    length1 = length + 1
				    session_cart.append({'image':str(detail.image), 'id':str(detail.id), 'length':str(length1), 'size':size, 'sex':detail.sex, 'quantity': str(quantity), 'unit_price':'1000', 'total_price':str(total_price)})
				    request.session['session_cart'] = session_cart
				except KeyError:
				    request.session['session_cart'] = [{'image':str(detail.image), 'id':str(detail.id), 'length':'1', 'size':size, 'sex':detail.sex, 'quantity': str(quantity), 'unit_price':'1000', 'total_price':str(total_price)}]
			return redirect('cart:viewCart')
	except IndexError:
		messages.info(request,'Item Is Unavailable, please select other sizes or check other items')
		return redirect('cart:viewCart')

	except Index.DoesNotExist:
		messages.info(request,'Item Is Unavailable, please select other sizes or check other items')
		return redirect('cart:viewCart')




def viewCart(request):
	try:
		qs = Cart.objects.filter(user=request.user, paid=False, ordered=False).order_by('-date')
		total = 0
		for i in qs:
			total = total + i.total_price
	except TypeError:
		try:
			total = 0
			session_cart = request.session['session_cart']
			qs = session_cart
			for i in qs:
			    total = total + int(i['total_price'])
		except KeyError:
			qs = []
			total = 0
			print('none')
	context = {'qs':qs, 'total':total}
	return render(request, 'cart/cart_list.html', context)

def delete_cart(request, id):
	try:
		qs = Cart.objects.get(id=id, user=request.user)
		qs.delete()
		return redirect('cart:viewCart')
	except TypeError:
		try:
			session_cart = request.session['session_cart']
			for i in session_cart:
				if i['length'] == str(id):
				    session_cart.remove(i)
				else:
					...
			request.session['session_cart'] = session_cart
			return redirect('cart:viewCart')
		except KeyError:
			return redirect('cart:viewCart')


def edit_cart(request):
    product_id = request.POST.get('editcart_id')
    product_quantity = request.POST.get('editcart_quantity')
    if request.user.is_authenticated:
        qs = get_object_or_404(Cart, id=int(product_id))
        qs.quantity = int(product_quantity)
        qs.total_price = int(product_quantity) * 1000
        qs.save()
        return redirect('cart:viewCart')
    else:
        session_cart = request.session['session_cart']
        for i in session_cart:
            if i['length'] == str(product_id):
                total_price = int(product_quantity) * 1000
                i['quantity'] = product_quantity
                i['total_price'] = str(total_price)

            else:
                ...
        request.session['session_cart'] = session_cart
        return redirect('cart:viewCart')

@login_required(login_url='/account/login_userpage/')
def order(request):
	qs = Cart.objects.filter(user=request.user, paid=False, ordered=False)
	total = 0
	for i in qs:
		total = total + i.total_price
	context = {'qs':qs, 'total':total}
	return render(request, 'cart/address.html', context)

def empty_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, paid=False, ordered=False)
        for i in cart:
            i.delete()
    else:
        request.session['session_cart'] = []
    return redirect('cart:viewCart')


@login_required(login_url='/account/login_userpage/') #this order is for delivery
def create_order(request):
	phone_number = request.POST.get('phone_number')
	address = request.POST.get('address')
	email = request.POST.get('email')
	if email == None or phone_number == None or address == None:
		return HttpResponse("Please Input details")
	else:
		orderproduct_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
		order = Order.objects.create(user=request.user, address=address, phone_number=phone_number, order_id=orderproduct_id, delivered=False, paid=False, email=email)
		cart = Cart.objects.filter(ordered=False, paid=False, user=request.user)
		for i in cart:
			i.order_key = order
			i.ordered=True
			i.save()
		return render(request, 'cart/confirmation.html', {'orderproduct_id':orderproduct_id})

@login_required(login_url='/account/login_userpage/') #this order is for pay
def create_order_pay(request):
	address = request.POST.get('address')
	phone_number = request.POST.get('phone_number')
	email = request.POST.get('email')
	if email == None or phone_number == None or address == None:
		return HttpResponse("Please Input details")
	else:
		orderproduct_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
		order = Order.objects.create(user=request.user, address=address, phone_number=phone_number, order_id=orderproduct_id, delivered=False, paid=True, email=email)
		cart = Cart.objects.filter(ordered=False, paid=False, user=request.user)
		for i in cart:
			i.order_key = order
			i.ordered=True
			i.paid = True
			i.save()
		return render(request, 'cart/confirmation.html', {'orderproduct_id':orderproduct_id})
