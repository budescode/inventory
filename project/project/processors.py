from administrator.models import Cart
from datetime import datetime
from cart.models import Cart
from index.models import IndexCategory

def PosterContextProcessors(request):
	try:
		date = datetime.today().strftime('%Y-%m-%d')
		sales_count = Cart.objects.filter(paid=True).count()
		cart = Cart.objects.filter(paid=False, user=request.user).count()
		total_price1 = Cart.objects.filter(paid=False, user=request.user)
		a = 0
		for i in total_price1:
			a = a+i.price

		sales_price1 = Cart.objects.filter(paid=True)
		b = 0
		for i in sales_price1:
			b = b+i.price

		return {'date':date ,'context_cart': cart, 'total_price':a, 'sales_count':sales_count, 'sales_price':b}
	except:
		return {'date':'date' ,'total_price':0, 'sales_count':0, 'sales_price':0}

def ProcessorUserCart(request):
	try:
		usercart_count1 = 0
		usercart_count = Cart.objects.filter(user=request.user, paid=False, ordered=False)
		for i in usercart_count:
			print('yeahh', i)
			usercart_count1 = usercart_count1 + i.quantity
		return {'usercart_count':usercart_count1}
	except:
		return {'usercart_count':0}

def ProcessorIndexCategory(request):
	allcategories = IndexCategory.objects.values('name').distinct()
	return {'allcategories':allcategories}