from django.contrib import admin
from .models import Index, IndexSize, IndexCategory, IndexSubCategory, Favourite


class IndexAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'subcategory', 'sex', 'price', 'stock', 'size']
    search_fields = ['name']

class IndexCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_count', 'id', 'image']
    search_fields = ['name']

class IndexSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['mycategory', 'name', 'total_count', 'id']


admin.site.register(Index, IndexAdmin)
admin.site.register(IndexSize)
admin.site.register(IndexCategory, IndexCategoryAdmin)
admin.site.register(IndexSubCategory, IndexSubCategoryAdmin)
admin.site.register(Favourite)


