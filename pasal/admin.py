from django.contrib import admin

# Register your models here.
from .models import Product, ProductType, Customer, Category, Sales



admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Sales)
admin.site.register(ProductType)
admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'product_type','primary_image','category'
              'product_code', 'price', 'available_quantity',)
    list_display = ('name', 'product_type', 'product_code','primary_image','category'
                    'price', 'available_quantity', 'created_date', 'updated_date','action_link')

    def action_link(self,obj):
        edit_link=('<a href="%d">Edit</a>' % obj.id)
        delete_link=('<a href="delete/%d">Delete</a>'  % obj.id)
        return edit_link + " " + delete_link
    action_link.allow_tags=True

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name')
    list_display=('name')

class CustomerAdmin(admin.ModelAdmin):
    fields = ('fullname','address')
    list_display = ('fullname','address')

class SalesAdmin(admin.ModelAdmin):
    fields = ('product','customer','quantity','sales_date')
    list_display = ('product','customer','quantity','sales_date')
              

class ProductTypeAdmin(admin.ModelAdmin):
    fields = ('product_type',)
    list_display = ('product_type', 'created_date', 'updated_date')


