from django.contrib import admin

# Register your models here.
from Magazin.models import Product, Category, Tag


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)

