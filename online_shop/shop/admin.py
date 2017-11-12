# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop.models import Product, ItemsInCart, Category





class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields if field.name[:3] != 'img']

	class Meta():
		model = Product

class ItemsIncartAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ItemsInCart._meta.fields]

	class Meta():
		model = ItemsInCart




admin.site.register(Product, ProductAdmin)
admin.site.register(ItemsInCart, ItemsIncartAdmin)
admin.site.register(Category)
