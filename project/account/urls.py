from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views



from django.contrib.auth.views import PasswordResetView

from django.urls import path


app_name = "account"
urlpatterns = [



	path('login/', views.login_page, name='login'),
	path('userlogout/', views.userlogout, name='userlogout'),

	path('login_dashboard/', views.login_dashboard, name='login_dashboard'),

	path('logout/', views.logout_page, name='logout'),
	path('logout_dashboard/', views.logout_dashboard, name='logout_dashboard'),

 	path('register/', views.register, name='register'),
	path('profile/', views.profile, name="profile" ),
	path('edit_profile/<slug:id>/', views.edit_profile, name="edit_profile" ),
	path('delete_profile/<slug:id>/', views.delete_profile, name="delete_profile" ),

	path('upgrade/', views.Upgrade, name="upgrade" ),
	path('register_success/', views.registration_success, name='registration_success'),
	path('change_password/', views.change_password, name='change_password'),
	path('change_password_confirm/', views.change_password_confirm, name='change_password_confirm'),
	path('<slug:pk>/<slug:username>/', views.change_password_code, name='change_password_code'),
	path('change_password_success/', views.change_password_success, name='change_password_success'),
	path('register_user/', views.register_user, name='register_user'),
	path('login_user/', views.login_user, name='login_user'),
	path('login_userpage/', views.login_userpage, name='login_userpage'),
	path('<slug:id>/', views.email_confirm, name='email_confirm'),




]

