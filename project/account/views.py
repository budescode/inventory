from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .forms import LoginForm, ChangePasswordCodeForm, ChangePasswordForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from datetime import *

from .models import Profile, ChangePasswordCode
# from django.shortcuts import get_list_or_404, get_object_or_404

# import urllib
# from django.core.mail import send_mail
from django.conf import settings
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import RegistrationConfirm
from cart.models import Cart
from index.models import Index

def register_user(request):
	username = request.POST.get('username')
	email = request.POST.get('email')
	password  = request.POST.get('password')
	user_check = User.objects.filter(username = username)
	email_check = User.objects.filter(email=email)
	if user_check.exists():
		return JsonResponse({'error':'username exists'})
	elif email_check.exists():
		return JsonResponse({'error':'email exists'})
	else:
		qs = User.objects.create_user(username, email, password)
		qs.is_active = False
		qs.save()
		reg = RegistrationConfirm.objects.create(username=qs)
		subject = "1kshop Email Confirmation"
		from_email = settings.EMAIL_HOST_USER
		# Now we get the list of emails in a list form.
		to_email = [email]
		#Opening a file in python, with closes the file when its done running
		detail2 = "https://www.1kshop.online/account/"+ str(reg.user_id) + '/'
		with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
			sign_up_message = sign_up_email_txt_file.read()
		message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
		html_template = get_template("account/emailconfirm.html").render({'detail2':detail2})
		message.attach_alternative(html_template, "text/html")
		message.send()
	return render(request, 'account/registration_success.html')


def email_confirm(request, id):
    qs = get_object_or_404(RegistrationConfirm, user_id = id)
    qs1 = qs.username
    qs1.is_active = True
    qs1.save()
    qs.delete()
    return render(request, 'account/emailconfirmsuccess.html')


def login_user(request):
	username  = request.POST.get("username")
	password  = request.POST.get("password")
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			try:
				session_cart = request.session['session_cart']
				if session_cart:
					for i in session_cart:
						qs = Index.objects.get(id=int(i['id']))
						Cart.objects.create(user=request.user, product=qs, size=i['size'], sex=i['sex'], quantity=i['quantity'], unit_price=int(i['unit_price']), total_price=int(i['total_price']))
				return JsonResponse({'response':'done'})
			except KeyError:
				return JsonResponse({'response':'done'})
		else:
			return JsonResponse({'error':'Disabled Account'})
	else:
		return JsonResponse({'error':'Invalid Details'})


def login_userpage(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		try:
			 			session_cart = request.session['session_cart']
			 			if session_cart:
			 				for i in session_cart:
			 					qs = Index.objects.get(id=int(i['id']))
			 					Cart.objects.create(user=request.user, product=qs, size=i['size'], sex=i['sex'], quantity=i['quantity'], unit_price=int(i['unit_price']), total_price=int(i['total_price']))
			 		except KeyError:
			 			...
			 		return redirect('home:home')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "account/loginuser.html", context)



def profile(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs=Profile.objects.all()
    return render(request, 'account/profile.html', {'qs':qs})




def register(request):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request, "account/registration_success.html")
    else:
        form = ProfileForm(request.POST or None)
    context = {"form": form}
    return render(request, "account/register.html", context)

def delete_profile(request, id):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs = Profile.objects.get(id=id)
    qs.delete()
    return redirect('account:profile')


def edit_profile(request, id):
    if request.user.username == 'cashier':
        return redirect('administrator:products')
    qs = Profile.objects.get(id=id)
    #if request.method == 'POST':
    form = ProfileForm(request.POST or None, request.FILES or None, instance=qs)
    if form.is_valid():

        name = form.cleaned_data.get('name')
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        photo = form.cleaned_data.get('description')
        qs.title = title
        qs.description = description
        qs.photo = photo
        qs.name = name
        qs.save()

        return redirect('account:profile')
    #else:
        #form = ProfileForm(request.POST or None, instance=qs)
    context = {"form": form}
    return render(request, "account/register.html", context)







def registration_success(request):
	return render(request, 'account/registration_success.html', {})


def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('administrator:administrator')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:

		form = LoginForm()
	context = {"form": form}
	return render(request, "account/login.html", context)


def login_dashboard(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('dashboard:dashboard')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:

		form = LoginForm()
	context = {"form": form}
	return render(request, "account/login_dashboard.html", context)


def logout_page(request):
	logout(request)
	return render(request, "account/logout.html", {})

def userlogout(request):
	logout(request)
	return redirect('home:home')

def logout_dashboard(request):
	logout(request)
	return render(request, "account/logout_dashboard.html", {})





def Upgrade(request):
	return render(request, 'account/upgrade.html')


def change_password(request):
	if request.method == 'POST':
		form = ChangePasswordCodeForm(request.POST)
		if form.is_valid():
			# try:
			username = form.cleaned_data.get('username')
			detail = ChangePasswordCode.objects.filter(username=username)
			if detail.exists():
				# messages.add_message(request, messages.INFO, 'invalid')
				for i in detail:
					i.delete()
				form.save()
				test = ChangePasswordCode.objects.get(username=username)
				try:
					user = User.objects.get(username=username)
					subject = "Change Password"
					from_email = settings.EMAIL_HOST_USER
					# Now we get the list of emails in a list form.
					to_email = [user.email]
					#Opening a file in python, with closes the file when its done running
					detail2 = "https://www.1kshop.online/account/"+ str(test.user_id) + '/' + username
					with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
						sign_up_message = sign_up_email_txt_file.read()
					message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
					html_template = get_template("account/change_password_email.html").render({'detail2':detail2})
					message.attach_alternative(html_template, "text/html")
					message.send()
					return redirect('account:change_password_confirm')
				except User.DoesNotExist:
					return HttpResponse('invalid username')
			else:
				form.save()
				try:
					user = User.objects.get(username=username)
					test = ChangePasswordCode.objects.get(username=username)
					subject = "Change Password"
					from_email = settings.EMAIL_HOST_USER
					# Now we get the list of emails in a list form.
					to_email = [user.email]
					#Opening a file in python, with closes the file when its done running
					detail2 = "https://www.1kshop.online/account/"+ str(test.user_id) + '/' + username
					with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
					    sign_up_message = sign_up_email_txt_file.read()
					message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
					html_template = get_template("account/change_password_email.html").render({'detail2':detail2})
					message.attach_alternative(html_template, "text/html")
					message.send()
					return redirect('account:change_password_confirm')
				except User.DoesNotExist:
					return HttpResponse('username does not exist')

		else:
			return HttpResponse('Invalid Email Address')
	else:
		form = ChangePasswordCodeForm()
	return render(request, 'account/change_password.html', {'form':form})


def change_password_confirm(request):
	return render(request, 'account/change_password_confirm.html', {})

def change_password_code(request, pk, username):
	try:
		test = ChangePasswordCode.objects.get(pk=pk)
		username = test.username
		try:
			u = User.objects.get(username=username)
			if request.method == 'POST':
				form = ChangePasswordForm(request.POST)
				if form.is_valid():
					u = User.objects.get(username=username)
					new_password = form.cleaned_data.get('new_password')
					confirm_new_password = form.cleaned_data.get('confirm_new_password')
					if new_password == confirm_new_password:
						u.set_password(confirm_new_password)
						u.save()
						test.delete()
						return redirect('account:change_password_success')
					else:
						return HttpResponse('your new password should match with the confirm password')
				else:
					return HttpResponse('Invalid Details')
			else:
				form = ChangePasswordForm()
		except User.DoesNotExist:
			return HttpResponse('invalid username, Usernames are case sensitive. Check the username properly and try again')
		return render(request, 'account/change_password_code.html', {'test':test, 'form':form, 'u':u, 'username':username})

	except ChangePasswordCode.DoesNotExist:
		return HttpResponse('disabled link')



def change_password_success(request):
	return render(request, 'account/change_password_success.html', {})