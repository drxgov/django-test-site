from django.contrib import admin
from .models import Category,product

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['name','category','slug','price','aviable','created','updated']
    list_filter = ['aviable','created','updated','category']
    list_editable = ['price','aviable']
    prepopulated_fields = {'slug':('name',)}