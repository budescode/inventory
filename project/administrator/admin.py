from django.contrib import admin

# Register your models here.
from .models import Category, MyItems, Cart, Image, SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_count']
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['mycategory', 'name', 'total_count']

admin.site.register(MyItems)
admin.site.register(Cart)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(SubCategory)




