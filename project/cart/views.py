from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from .models import Cart
from order.models import Order
from index.models import Index, IndexSize, IndexCategory, IndexSubCategory
import string
import random
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url='/account/login/')
def addtoCart(request):
	product_id = request.POST.get('product_id')

	detail = Index.objects.get(id=int(product_id))
	size = request.POST.get('size')
	sex = request.POST.get('sex')
	quantity = request.POST.get('quantity')
	total_price = 1000 * int(quantity)
	print(product_id, detail, size, sex)
	Cart.objects.create(product=detail, size=size, sex=sex, quantity=int(quantity), user=request.user, paid=False, unit_price=1000, total_price=total_price)
	return JsonResponse({'response':'done'})


@login_required(login_url='/account/login/')	
def viewCart(request):
	qs = Cart.objects.filter(user=request.user, paid=False, ordered=False)
	total = 0
	for i in qs:
		total = total + i.total_price
	context = {'qs':qs, 'total':total}
	return render(request, 'cart/cart_list.html', context)

def delete_cart(request, id):
	qs = Cart.objects.get(id=id)
	qs.delete()
	qs.save()
	return redirect('cart:viewCart')

@login_required(login_url='/account/login/')
def order(request):
	return render(request, 'cart/address.html')

@login_required(login_url='/account/login/')
def create_order(request):
	address = request.POST.get('address')
	phone_number = request.POST.get('phone_number')
	if address == None or phone_number == None:
		return HttpResponse("Please Input details")
	else:		
		orderproduct_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
		order = Order.objects.create(user=request.user, address=address, phone_number=phone_number, order_id=orderproduct_id, delivered=False, paid=False)
		cart = Cart.objects.filter(ordered=False, paid=False, user=request.user)
		print(order)
		for i in cart:
			i.order_key = order
			i.ordered=True
			i.save()
		return render(request, 'cart/confirmation.html', {'orderproduct_id':orderproduct_id})
