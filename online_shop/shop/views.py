# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from shop.models import Product

def catalog(request, page):
	items = Product.objects.all()
	range_slice = int(page) * 30
	returned_items = items[range_slice-30 : range_slice]
	context = {
		'items': returned_items,
	}

	return render(request, 'catalog.html', context)

def item(request, pk):
	item = Product.objects.get(id=pk)

	context = {
		'item': item,
	}

	return render(request, 'item.html', context)

def cart(request):
	request.session['test'] = 'test!!!!!!!!!!'
	print(request.session.items())
	# ids = [ int(x) for x in request.session['order'].split()]
	# order = [Product.objects.get(id=x) for x in ids]

	context = {
		# 'items': order,
		'test': request.session['test']
	}

	return render(request, 'cart.html', context)

