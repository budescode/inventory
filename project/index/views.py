from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
import json
from django.db.models import Q
import barcode
from .models import Index, IndexSize, IndexCategory, IndexSubCategory
from order.models import Order

def home(request):
	Tshirt_subcategory = IndexSubCategory.objects.filter(name__iexact = 'T-Shirt')[0]
	polo_subcategory = IndexSubCategory.objects.filter(name__iexact = 'Polo')[0]
	jean_subcategory = IndexSubCategory.objects.filter(name__iexact = 'Jean')[0]
	trouser_category = IndexCategory.objects.filter(name__iexact='Trouser')[0]

	tshirt = Index.objects.filter(subcategory=Tshirt_subcategory)
	polo = Index.objects.filter(subcategory=polo_subcategory)
	jean = Index.objects.filter(subcategory=jean_subcategory)
	trouser = Index.objects.filter(category=trouser_category)

	context = {'tshirt':tshirt, 'polo':polo, 'jean':jean, 'trouser':trouser}
	return render(request, 'index/index.html', context)

def detail(request, id):
	detail = get_object_or_404(Index ,id=id)
	qs = Index.objects.filter(subcategory=detail.subcategory)
	context = {'qs':qs, 'detail':detail}
	return render(request, 'index/product_detail.html', context)

def filter_category(request, id):
	detail = get_object_or_404(IndexCategory ,id=id)
	qs = Index.objects.filter(category=detail)
	context = {'qs':qs, 'detail':detail}
	return render(request, 'index/category.html', context)

def filter_subcategory(request, id):
	detail = get_object_or_404(IndexSubCategory ,id=id)
	qs = Index.objects.filter(subcategory=detail)
	context = {'qs':qs, 'detail':detail}
	return render(request, 'index/subcategory.html', context)


def filter_unisex_category(request, category, unisex):
	detail = get_object_or_404(IndexCategory , name__iexact=category, unisex__iexact = unisex)
	qs = detail.index_category.all()
	context = {'qs':qs}
	return render(request, 'index/filter_unisex.html', context)

def filter_unisex_subcategory(request, category, subcategory, unisex):
	category = get_object_or_404(IndexCategory, name__iexact=category, unisex__iexact = unisex)
	subcategory = get_object_or_404(IndexSubCategory, mycategory = category, name__iexact=subcategory)
	qs = subcategory.index_subcategory.all()
	context = {'qs':qs}
	return render(request, 'index/filter_unisex.html', context)


def filter_allcategory(request, name):
	list_item = []
	detail = IndexCategory.objects.filter(name=name)
	for i in detail:
		qs = Index.objects.filter(category=i)
		list_item.extend(qs)
	context = {'detail':detail, 'list_item':list_item}
	return render(request, 'index/filter_category.html', context)


def about(request):
	return render(request, 'rough.html')

def contact(request):
	return render(request, 'contact.html')

def blog(request):
	return render(request, 'blog.html')

