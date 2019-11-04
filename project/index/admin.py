from django.contrib import admin
from .models import Index, IndexSize, IndexCategory, IndexSubCategory


class IndexAdmin(admin.ModelAdmin):
    list_display = ['sex', 'price', 'stock', 'size', 'category', 'subcategory']

class IndexCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'unisex', 'total_count']

class IndexSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['mycategory', 'name', 'total_count']
 

admin.site.register(Index, IndexAdmin)
admin.site.register(IndexSize)
admin.site.register(IndexCategory, IndexCategoryAdmin)
admin.site.register(IndexSubCategory, IndexSubCategoryAdmin)

