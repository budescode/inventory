from django.contrib import admin

# Register your models here.
from .models import Category, MyItems, Cart, Image

admin.site.register(MyItems)
admin.site.register(Cart)
admin.site.register(Image)
admin.site.register(Category)






