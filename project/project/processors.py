from administrator.models import Cart
from datetime import datetime

from index.models import IndexCategory

def PosterContextProcessors(request):
	try:
		date = datetime.today().strftime('%Y-%m-%d')
		sales_count = Cart.objects.filter(paid=True).count()
		cart = Cart.objects.filter(paid=False, user=request.user)
		total_price1 = Cart.objects.filter(paid=False, user=request.user)
		price = 0
		total = 0
		for i in cart:
			price = price + i.price
			total = total + i.qty
		return {'date':date ,'context_cart': total, 'total_price':price}
	except:
		return {'date':date ,'total_price':0, 'sales_count':0, 'sales_price':0}

def ProcessorUserCart(request):
	from cart.models import Cart
	#del request.session['session_cart']
	if request.user.is_authenticated:
		usercart_count1 = 0
		usercart_count = Cart.objects.filter(user=request.user, paid=False, ordered=False)
		for i in usercart_count:
			usercart_count1 = usercart_count1 + i.quantity
		return {'usercart_count':usercart_count1}
	else:
		usercart_count1 = 0
		try:
		    session_cart = request.session['session_cart']
		    for i in session_cart:
		        usercart_count1 = usercart_count1 + int(i['quantity'])
		except KeyError :
			usercart_count1 = 0
		return {'usercart_count':usercart_count1}




def ProcessorIndexCategory(request):
	allcategories = IndexCategory.objects.all()
	return {'allcategories':allcategories}