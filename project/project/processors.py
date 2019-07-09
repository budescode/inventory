from administrator.models import Cart
def PosterContextProcessors(request):
	sales_count = Cart.objects.filter(paid=True).count()
	cart = Cart.objects.filter(paid=False).count()
	total_price1 = Cart.objects.filter(paid=False)
	a = 0
	for i in total_price1:
		a = a+i.price

	sales_price1 = Cart.objects.filter(paid=True)
	b = 0
	for i in sales_price1:
		b = b+i.price

	return {'context_cart': cart, 'total_price':a, 'sales_count':sales_count, 'sales_price':b}