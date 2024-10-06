from django.contrib import admin

# Register your models here.

from . models import product
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['title','selling_price','discounted_price','description','composition','category','product_image']
    
# admin.site.register(News, NewsAdmin)