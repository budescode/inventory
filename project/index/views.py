from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from .forms import PosterForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
# from account.forms import CreateProfileForm, CategoryForm
# from account.models import CreateProfile, Profile
from .models import Poster
import json
from administrator.models import CountryDetails
from django.db.models import Q


def home(request):
	qs = CountryDetails.objects.all()

	return render(request, 'index.html', {'qs':qs})

def about(request):
	return render(request, 'rough.html')

def contact(request):
	return render(request, 'contact.html')

def blog(request):
	return render(request, 'blog.html')


# this function is used to filter the searched items from users
def filter_search(request):
	hiddensearch = request.POST.get("hiddensearch") #it brings a string of the postalcode
	hiddensearch1 =  hiddensearch.split('X')

	propertytype1 = request.POST.get("propertytype1")		
	propertytype1 =  propertytype1.split(',')
	# print(propertytype1, 'propertytypw')
	bedmin1 = request.POST.get("bedmin1")

	bedmax1 = request.POST.get("bedmax1")	
	pricemax1 = request.POST.get("pricemax1")
	pricemax1 = ''.join(pricemax1.split())
	pricemax1 = ''.join(pricemax1.split(','))
	pricemax1 = pricemax1[1:]
	# print(pricemax1)



	pricemin1 = request.POST.get("pricemin1")	
	pricemin1 = ''.join(pricemin1.split())
	pricemin1 = ''.join(pricemin1.split(','))
	pricemin1 = pricemin1[1:]
	print(pricemax1, pricemin1, bedmax1, bedmin1)

	if bedmin1 == 'B' or bedmin1 == 'A':
		bedminsearch = 0
	elif bedmin1 == 'S':
		bedminsearch = 0
	else:
		bedminsearch = bedmin1

	if bedmax1 == 'B' or bedmax1 == 'A':
		bedmaxsearch = 100

	elif bedmax1 == 'S':
		bedmaxsearch = 0

	else:
		bedmaxsearch = bedmax1

	if pricemin1 == 'rice(min)' or pricemin1 == 'ny':
		priceminsearch = 0
	else:
		priceminsearch = int(pricemin1)

	if pricemax1 == 'rice(max)' or pricemax1 == 'ny':
		pricemaxsearch = 1000000000000
	else:
		pricemaxsearch = int(pricemax1)



	# print(bedmax1, bedmaxsearch)
	if bedmaxsearch==20:
		test = Poster.objects.filter(Bedrooms__gte=bedminsearch, postcode=804)
	else:
		test = Poster.objects.filter(Bedrooms__lte=bedmaxsearch, Bedrooms__gte=bedminsearch,postcode=804)

	if pricemaxsearch==20:
		test1 = Poster.objects.filter(Q(Price__gte=priceminsearch) & Q(postcode=804))
	else:
		test1 = Poster.objects.filter(Q(Price__lte=pricemaxsearch), Q(Price__gte=priceminsearch) & Q(postcode=804))


	generallist = []
	# this is the list where all the filtered items will be 
	
	mylist = list(dict.fromkeys(hiddensearch1))
	# it'll remove duplicate from the list that has the postal code

	searchlist = []	
	# this list contains all the Poster that has the postal code needed
	mylist = ['NT DARWIN', 'TAS GLEBE']
	for i in mylist:
		findvalue = i.find(' ')
		state = i[0:findvalue].strip()
		suburb = i[findvalue+1:].strip()

		
		post = Poster.objects.filter(state=state, suburb=suburb)
		if post:
			searchlist.extend(post)

	
	searchlist = list(dict.fromkeys(searchlist))
	# print('searchlist', searchlist, len(searchlist))
	# print(bedminsearch, bedmaxsearch, priceminsearch, pricemaxsearch)
	for i in searchlist:
		
		if propertytype1[0]=='' or propertytype1[0]== 'All property types':			
			if int(i.Bedrooms) >= int(bedminsearch) and int(i.Bedrooms) <= int(bedmaxsearch) and int(i.Price)>=priceminsearch and int(i.Price)<=pricemaxsearch:
				print("yes", i.Property_type, i.Price)
				generallist.append(i)
			else:
				pass

			# it'll append the post to the general list
		else:
			for a in propertytype1:
				if i.Property_type==a and int(i.Bedrooms) >= int(bedminsearch) and int(i.Bedrooms) <= int(bedmaxsearch) and int(i.Price)>=priceminsearch and int(i.Price)<=pricemaxsearch:
					print("yes", i.Property_type)
					generallist.append(i)


	generallist = list(dict.fromkeys(generallist))
	# it'll remove duplicate from the generallist

	print(generallist)
	context = {'generallist':generallist, 'bedminsearch':bedminsearch, 'bedmaxsearch':bedmaxsearch, 'priceminsearch':priceminsearch, 'pricemaxsearch':pricemaxsearch}
	return render(request, 'filter_search.html', context)

# batmobi748/






@login_required(login_url='/account/login/')
def post(request):
	# qs = CountryDetails.objects.all()
	state = CountryDetails.objects.values_list('state', flat=True).distinct()
	
	# for i in qs:
	# 	print(qs)
	user = User.objects.get(username=request.user.username)
	if request.method == 'POST':		
		form = PosterForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			qs = form.save(commit=False)
			
			user = User.objects.get(username=request.user.username)
			qs.user = user
			qs.save()
			return render(request, 'post_success.html')
	else:
		form = PosterForm() 
	context = {"state": state, 'form':form}
	return render(request, "sell.html", context)



def filterDetails(request):
	state = request.POST.get("state")
	print(state)
	# .order_by('photo__name', 'photo__url').distinct('photo__name', 'photo__url')
	qs = CountryDetails.objects.filter(state__iexact=state).values_list('postcode', 'suburb').distinct()
	qs1 = CountryDetails.objects.filter(state__iexact=state)

	print(len(qs), len(qs1))
	result_list = list(qs.values('suburb', 'postcode'))
	return HttpResponse(json.dumps(result_list))



@login_required(login_url='/account/login/')
def Mypost(request):
	user = User.objects.get(username=request.user.username)
	qs = Poster.objects.filter(active=False, user=user)
	context = {'qs':qs}
	return render(request, "mypost.html", context)


def Delete(request, id):
	user = User.objects.get(username=request.user.username)
	try:
		qs = Poster.objects.get(id_user=id,  user=user)
		qs.delete()
	except Poster.DoesNotExist:
		return HttpResponse("Post does not exist")
	return redirect('home:mypost')

def Edit(request, id):
	user = User.objects.get(username=request.user.username)
	qs = Poster.objects.get(id_user=id,  user=user)
	if request.method == 'POST':		
		form = PosterForm(request.POST or None, request.FILES or None, instance=qs)
		if form.is_valid():
			qs = form.save(commit=False)
			
			user = User.objects.get(username=request.user.username)
			qs.user = user
			qs.save()
			return render(request, 'editpost_success.html')


	else:
		form = PosterForm(request.POST or None, request.FILES or None, instance=qs)
	context = {"form": form}
	return render(request, "editpost.html", context)
