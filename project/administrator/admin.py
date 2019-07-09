from django.contrib import admin

# Register your models here.
from .models import CountryDetails, MyItems, Cart
admin.site.register(CountryDetails)

admin.site.register(MyItems)
admin.site.register(Cart)




