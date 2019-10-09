from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
import json
from django.db.models import Q
import barcode


def home(request):
	return render(request, 'index/index.html')

def about(request):
	return render(request, 'rough.html')

def contact(request):
	return render(request, 'contact.html')

def blog(request):
	return render(request, 'blog.html')

