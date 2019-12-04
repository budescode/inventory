from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
import json
from django.db.models import Q
import barcode
from .models import Index, IndexSize, IndexCategory, IndexSubCategory, Favourite
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives



def home(request):
	Tshirt_subcategory = IndexSubCategory.objects.filter(name__iexact = 'T-Shirt')[0]
	polo_subcategory = IndexSubCategory.objects.filter(name__iexact = 'Polo')[0]
	jean_subcategory = IndexSubCategory.objects.filter(name__iexact = 'Jean')[0]
	trouser_category = get_object_or_404(IndexCategory, name__iexact = 'Trouser')
	fleece_category = get_object_or_404(IndexCategory, name__iexact = 'Fleece')
	jumpers_category = get_object_or_404(IndexCategory, name__iexact = 'Jumpers')
	underwear_category = get_object_or_404(IndexCategory, name__iexact = 'Underwear')
	tie_category = get_object_or_404(IndexCategory, name__iexact = 'Tie')
	shorts_category = get_object_or_404(IndexCategory, name__iexact = 'Shorts')
	socks_category = get_object_or_404(IndexCategory, name__iexact = 'Socks')
	sleeves_category = get_object_or_404(IndexCategory, name__iexact = 'Sleeves')
	hats_category = get_object_or_404(IndexCategory, name__iexact = 'Hats')
	category = IndexCategory.objects.all()
	tshirt = []
	tshirt_list = []
	for i in Index.objects.filter(subcategory=Tshirt_subcategory):
		if i.name not in tshirt_list:
		    if len(tshirt_list)!=25:
		        tshirt_list.append(i.name)
		        tshirt.append(i)

	polo = []
	polo_list = []
	for i in Index.objects.filter(subcategory=polo_subcategory):
		if i.name not in polo_list:
		    if len(polo_list)!=25:
		        polo_list.append(i.name)
		        polo.append(i)

	jean = []
	jean_list = []
	for i in Index.objects.filter(subcategory=jean_subcategory):
		if i.name not in jean_list:
		    if len(jean_list)!=25:
		        jean_list.append(i.name)
		        jean.append(i)

	trouser = []
	trouser_list = []
	for i in Index.objects.filter(category=trouser_category):
		if i.name not in trouser_list:
		    if len(trouser_list)!=25:
		        trouser_list.append(i.name)
		        trouser.append(i)

	fleece = []
	fleece_list = []
	for i in Index.objects.filter(category=fleece_category):
		if i.name + i.color not in fleece_list:
		    if len(fleece_list)!=25:
		        fleece_list.append(i.name + i.color)
		        fleece.append(i)
	jumpers = []
	jumpers_list = []
	for i in Index.objects.filter(category=jumpers_category):
		if i.name + i.color not in jumpers_list:
		    if len(jumpers_list)!=25:
		        jumpers_list.append(i.name + i.color)
		        jumpers.append(i)
	underwear = []
	underwear_list = []
	for i in Index.objects.filter(category=underwear_category):
		if i.name + i.color not in underwear_list:
		    if len(underwear_list)!=25:
		        underwear_list.append(i.name + i.color)
		        underwear.append(i)
	shorts = []
	shorts_list = []
	for i in Index.objects.filter(category=shorts_category):
		if i.name + i.color not in shorts_list:
		    if len(shorts_list)!=25:
		        shorts_list.append(i.name + i.color)
		        shorts.append(i)
	sleeves = []
	sleeves_list = []
	for i in Index.objects.filter(category=sleeves_category):
		if i.name + i.color not in sleeves_list:
		    if len(sleeves_list)!=25:
		        sleeves_list.append(i.name + i.color)
		        sleeves.append(i)
	tie = []
	tie_list = []
	for i in Index.objects.filter(category=tie_category):
		if i.name + i.color not in tie_list:
		    if len(tie_list)!=25:
		        tie_list.append(i.name + i.color)
		        tie.append(i)
	socks = []
	socks_list = []
	for i in Index.objects.filter(category=socks_category):
		if i.name + i.color not in socks_list:
		    if len(socks_list)!=25:
		        socks_list.append(i.name + i.color)
		        socks.append(i)

	context = {'trouser':trouser,'tshirt':tshirt, 'polo':polo, 'jean':jean,'fleece':fleece, 'category':category, 'jumpers':jumpers, 'underwear':underwear, 'shorts':shorts, 'sleeves':sleeves, 'tie':tie, 'socks':socks}
	return render(request, 'index/index.html', context)

def detail(request, id):
	detail = get_object_or_404(Index ,id=id)
	#qs = Index.objects.filter(subcategory=detail.subcategory)
	qs_name = []
	qs = []
	others = []
	others_list = []
	for i in Index.objects.filter(subcategory=detail.subcategory):
		if i.name not in qs_name:
			qs_name.append(i.name)
			qs.append(i)
	for i in Index.objects.filter(subcategory=detail.subcategory, name=detail.name):
		if i.color not in others_list:
			others_list.append(i.color)
			others.append(i)
	color = Index.objects.filter(category=detail.category, subcategory=detail.subcategory, name=detail.name).values_list('color', flat=True).distinct()
	context = {'qs':qs, 'detail':detail, 'color':color, 'others':others}
	return render(request, 'index/product_detail.html', context)




def addtoFavourite(request, id):
    qs = Index.objects.get(id=int(id))
    Favourite.objects.create(user=request.user, product_id=qs)
    return JsonResponse({'done':'done'})


def myFavourite(request):
    qs = Favourite.objects.filter(user=request.user)
    context = {'qs':qs}
    return render(request, 'index/favourite.html', context)

def deletemyFavourite(request, id):
    qs = get_object_or_404(Favourite, id=id)
    qs.delete()
    return redirect('home:myFavourite')

def faq(request):
    return render(request, 'index/faq.html')

def customer_service(request):
    return render(request, 'index/customer_service.html')

def orders_and_returns(request):
    return render(request, 'index/orders_and_returns.html')

def filter_male(request):
	qs = Index.objects.filter(sex="Male")
	context = {'qs':qs}
	return render(request, 'index/filter_unisex.html', context)


def filter_category(request, id):
	detail = get_object_or_404(IndexCategory ,id=id)
	qs = []
	list_item1 = []
	for i in Index.objects.filter(category=detail).all():
		if i.name not in list_item1:
			qs.append(i)
			list_item1.append(i.name)
	context = {'qs':qs, 'detail':detail}
	return render(request, 'index/category.html', context)

def filter_subcategory(request, id):
	detail = get_object_or_404(IndexSubCategory ,id=id)
	qs = []
	list_item1 = []
	for i in Index.objects.filter(subcategory=detail).all():
		if i.name not in list_item1:
			qs.append(i)
			list_item1.append(i.name)
	context = {'qs':qs, 'detail':detail}
	return render(request, 'index/subcategory.html', context)


def filter_unisex_category(request, category, unisex):
	detail = get_object_or_404(IndexCategory , name__iexact=category)
	list_item = []
	list_item1 = []
	for i in Index.objects.filter(category=detail, sex=unisex).all():
		if i.name + i.color + i.sex not in list_item1:
			list_item.append(i)
			list_item1.append(i.name + i.color + i.sex)
	paginator = Paginator(list_item, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	qs = paginator.get_page(page)
	context = {'qs':qs}
	return render(request, 'index/filter_unisex.html', context)

def filter_unisex_subcategory(request, category, subcategory, unisex):
	category = get_object_or_404(IndexCategory, name__iexact=category)
	subcategory = get_object_or_404(IndexSubCategory, mycategory = category, name__iexact=subcategory)
	list_item = []
	list_item1 = []
	for i in Index.objects.filter(sex__iexact=unisex, category=category, subcategory=subcategory).all():
		if i.name + i.color + i.sex not in list_item1:
			list_item.append(i)
			list_item1.append(i.name + i.color + i.sex)
	paginator = Paginator(list_item, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	qs = paginator.get_page(page)
	context = {'qs':qs, 'category':category, 'subcategory':subcategory}
	return render(request, 'index/filter_unisex.html', context)


def filtersearch_unisex_subcategory(request):
	if request.method == 'POST':
		category_name = request.POST.get('select_cat')
		request.session['category_name'] = category_name
		subcategory_name = request.POST.get('select_subcat')
		request.session['subcategory_name'] = subcategory_name
		size = request.POST.get('select_cat_size')
		request.session['size'] = size
		sex = request.POST.get('select_cat_sex')
		request.session['sex'] = sex
	else:
		category_name = request.session['category_name']
		subcategory_name = request.session['subcategory_name']
		size = request.session['size']
		sex = request.session['sex']
	category = get_object_or_404(IndexCategory, name__iexact=category_name)
	subcategory = get_object_or_404(IndexSubCategory, mycategory = category, name__iexact=subcategory_name)
	list_item = []
	list_item1 = []
	if sex == 'Any' and size == 'Any':
		for i in Index.objects.filter(category=category,subcategory=subcategory).all():
			if i.name + i.color not in list_item1:
				list_item.append(i)
				list_item1.append(i.name + i.color)
	elif sex == "Any" and size != 'Any':
		for i in Index.objects.filter(category=category,subcategory=subcategory, size=size).all():
			if i.name not in list_item1:
				list_item.append(i)
				list_item1.append(i.name)
	elif sex != "Any" and size == 'Any':
		for i in Index.objects.filter(category=category,subcategory=subcategory, sex=sex).all():
			if i.name not in list_item1:
				list_item.append(i)
				list_item1.append(i.name)
	elif sex != 'Any' and size != 'Any':
		for i in Index.objects.filter(category=category,subcategory=subcategory, sex=sex, size=size).all():
			if i.name not in list_item1:
				list_item.append(i)
				list_item1.append(i.name)
	else:
		list_item = []
	paginator = Paginator(list_item, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	qs = paginator.get_page(page)
	context = {'qs':qs, 'category':category, 'subcategory':subcategory}
	return render(request, 'index/filter_unisex.html', context)




def search(request):
	if request.method == 'POST':
		searchitem = request.POST.get('searchitem')
		print('searchitem', searchitem)
		request.session['searchitem'] = searchitem
	else:
		try:
			searchitem = request.session['searchitem']
		except:
			return HttpResponse('invalid response')
	list_item = []
	list_item1 = []
	try:
		category = get_object_or_404(IndexCategory, name__icontains=searchitem)
		qs = Index.objects.filter(category=category)
		for i in qs:
		    if i.name + i.color not in list_item1:
		        list_item.append(i)
		        list_item1.append(i.name + i.color)
	except:
	    ...
	try:
		subcategory = get_object_or_404(IndexSubCategory, name__icontains=searchitem)
		qs = Index.objects.filter(subcategory = subcategory)
		for i in qs:
			if i.name + i.color not in list_item1:
				list_item.append(i)
				list_item1.append(i.name + i.color)
	except:
		...
	paginator = Paginator(list_item, 25) # Show 25 contacts per page

	try:
		qs = Index.objects.filter(name__icontains=searchitem)
		for i in qs:
			if i.name + i.color not in list_item1:
				list_item.append(i)
				list_item1.append(i.name + i.color)
	except:
		...

	try:
		qs = Index.objects.filter(color__icontains=searchitem)
		for i in qs:
			if i.name + i.color not in list_item1:
				list_item.append(i)
				list_item1.append(i.name + i.color)
	except:
		...

	paginator = Paginator(list_item, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	qs = paginator.get_page(page)
	context = {'qs':qs}
	return render(request, 'index/search.html', context)


# 	category = get_object_or_404(IndexCategory, name__iexact=searchitem)
# 	subcategory = get_object_or_404(IndexSubCategory, mycategory = category, name__iexact=subcategory_name)


# 	paginator = Paginator(list_item, 25) # Show 25 contacts per page
# 	page = request.GET.get('page')
# 	qs = paginator.get_page(page)
	#context = {'qs':qs, 'category':category, 'subcategory':subcategory}
# 	return render(request, 'index/search.html', context)






def filter_allcategory(request, name): #this view will get all categories
	list_item = []
	list_item1 = []
	detail = IndexCategory.objects.filter(name=name)[0]
	for i in Index.objects.filter(category=detail).all():
		if i.name + i.color not in list_item1:
			list_item.append(i)
			list_item1.append(i.name + i.color)
	paginator = Paginator(list_item, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	qs = paginator.get_page(page)
	context = {'detail':detail, 'qs':qs, 'name':name}
	return render(request, 'index/filter_category.html', context)

def filtersearch_allcategory(request): #this view will filter categories by size or sex
	if request.method == 'POST':
		category = request.POST.get('select_cat')
		request.session['category'] = category
		size = request.POST.get('select_cat_size')
		request.session['size'] = size
		sex = request.POST.get('select_cat_sex')
		request.session['sex'] = sex
	else:
		category = request.session['category']
		size = request.session['size']
		sex = request.session['sex']
	name = get_object_or_404(IndexCategory, name=category)
	list_item = []
	list_item1 = []
	if sex == 'Any' and size == 'Any':
	    for i in  Index.objects.all():
	        if i.name + i.color not in list_item1:
	            list_item.append(i)
	            list_item1.append(i.name + i.color)
	elif sex == "Any" and size != 'Any':
	    for i in  Index.objects.filter(category=name, size=size).all():
	        if i.name + i.color not in list_item1:
	            list_item.append(i)
	            list_item1.append(i.name + i.color)
	elif sex != "Any" and size == 'Any':
	    for i in  Index.objects.filter(category=name, sex=sex).all():
	        if i.name + i.color not in list_item1:
	            list_item.append(i)
	            list_item1.append(i.name + i.color)
	else:
	    list_item = []

	paginator = Paginator(list_item, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	qs = paginator.get_page(page)
	context = {'qs':qs, 'sex':sex, 'size':size, 'name':name}
	return render(request, 'index/filtersearch_allcategory.html', context)



def about(request):
	return render(request, 'rough.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		comment = request.POST.get('comment')
		messages.info(request,'Email succesfully sent, we will get back to you shortly')
		subject, from_email, to = '1k shop customer email', email, 'info@yehgs.co.uk'
		text_content = 'This is an important message.'
		html_content = '<p>' + 'email : </br>' + email +  '</p>' + '<p>' + 'name : </br>' + name +  '</p>' + '<p>'+ 'Message : </br>'  + comment + '</p> <br>'
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		return redirect('home:contact')
	return render(request, 'index/contact.html')


def terms(request):
	return render(request, 'index/terms.html')

