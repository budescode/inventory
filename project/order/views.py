from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.contrib.auth.decorators import login_required
from cart.models import Cart

@login_required(login_url='/account/login/')
def myorder(request):
    qs = Order.objects.filter(user=request.user).order_by('-date', '-time')
    context = {'qs':qs}
    return render(request, 'order/index.html', context)

@login_required(login_url='/account/login/')
def deletemyorder(request, id):
    qs = get_object_or_404(Order, id=id, user=request.user)
    qs.delete()
    return redirect('order:myorder')

def orderdetails(request, id):
    order =  get_object_or_404(Order, id=id, user=request.user)
    qs = order.order_name.all().order_by('-date', '-time')
    context = {'qs':qs, 'order':order}
    return render(request, 'order/order_details.html', context)

def deletemyordereditems(request, id, order_id):
    cart =  get_object_or_404(Cart, id=id, user=request.user)
    cart.delete()
    return redirect('order:orderdetails', order_id)
