from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse ,QueryDict
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, CategoryForm, ChangePasswordCodeForm, ChangePasswordForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import *

from .models import Profile, ChangePasswordCode
from django.shortcuts import get_list_or_404, get_object_or_404

import urllib
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

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





# if request.method == "POST":
# 	user_form = UserForm(request.POST, request.FILES, instance=user)
# 	formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

# 		if user_form.is_valid():
# 			created_user = user_form.save(commit=False)
# 			formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

# 				if formset.is_valid():
# 					created_user.save()
# 					formset.save()
# 					return HttpResponseRedirect('/accounts/profile/')



def registration_success(request):
	return render(request, 'account/registration_success.html', {})

valuenext = ''
def login_page(request):
	if request.method == 'POST':
		# redirect_to = request.GET.get('next', '')
		# valuenext= "http://127.0.0.1:8000"+redirect_to
		# print(redirect_to, 'but', valuenext)

		form = LoginForm(request.POST or None)
		if form.is_valid():
			phone_number  = form.cleaned_data.get("phone_number")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=phone_number, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		# print("value is", valuenext)
			 #		return HttpResponseRedirect(valuenext)
			 		return redirect('administrator:administrator')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:

		form = LoginForm()
	context = {"form": form}
	return render(request, "account/login.html", context)


def logout_page(request):
	logout(request)
	return render(request, "account/logout.html", {})




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
				subject = "Change Password"
				from_email = settings.EMAIL_HOST_USER
				# Now we get the list of emails in a list form.
				to_email = ['aceplayhousehq@gmail.com']
				#Opening a file in python, with closes the file when its done running
				detail2 = "http://budescode.pythonanywhere.com/account/"+ str(test.user_id) + '/' + username
				with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
				    sign_up_message = sign_up_email_txt_file.read()
				message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
				html_template = get_template("account/change_password_email.html").render({'detail2':detail2})
				message.attach_alternative(html_template, "text/html")
				message.send()
				return redirect('account:change_password_confirm')
			else:
				form.save()
				test = ChangePasswordCode.objects.get(username=username)
				subject = 'Change Password'
				from_email= settings.EMAIL_HOST_USER
				to_email = ['aceplayhousehq@gmail.com']

				html = "http://budescode.pythonanywhere.com/account/"+ str(test.user_id) + '/' + username
				message = 'hi, click on the link below to change your password' + html
				send_mail(subject, message, from_email, to_email, fail_silently = False )
				return redirect('account:change_password_confirm')

		else:
			return HttpResponse('Invalid Email Address')
	else:
		form = ChangePasswordCodeForm()
	return render(request, 'account/change_password.html', {'form':form})


def change_password_confirm(request):
	return render(request, 'account/change_password_confirm.html', {})
def change_password_code(request, pk, username):
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
	return render(request, 'account/change_password_code.html', {'test':test, 'form':form, 'u':u})



def change_password_success(request):
	return render(request, 'account/change_password_success.html', {})