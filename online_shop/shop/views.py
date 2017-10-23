# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from shop.models import Product
from django.http import JsonResponse
from .models import ItemsInCart, Product

def catalog(request):
	items = Product.objects.all()
	# range_slice = int(page) * 30
	# returned_items = items[range_slice-30 : range_slice]
	context = {
		# 'items': returned_items,
	}

	return render(request, 'shop.html', context)

def item(request, pk):
	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()
	item = Product.objects.get(id=pk)

	context = {
		'item': item,
	}

	return render(request, 'shop-single.html', context)

def cart(request):
	# session_key = request.session.session_key

	# if not session_key:
	# 	session_key = request.session.cycle_key()

	return render(request, 'cart.html')


def cart_adding_ajax(request):
	session_key = request.session.session_key

	ret_dict = dict()


	data = request.POST
	items_id = Product.objects.get(id=data.get('items_id'))
	amount = data.get('amount')

	new_order_in_cart, created = ItemsInCart.objects.get_or_create(session_key=session_key, item=items_id, defaults={'amount':amount})
	if not created:
		new_order_in_cart.amount += int(amount)
		new_order_in_cart.save(force_update=True)

	items_in_cart = ItemsInCart.objects.filter(session_key=session_key, is_active=True)
	total_amount = items_in_cart.count()

	ret_dict['total_amount'] = total_amount

	ret_dict['item'] = []



	for item in items_in_cart:
		item_dict = dict()
		item_dict['title'] = item.item.title
		item_dict['amount'] = item.amount
		item_dict['img_url'] = item.item.img1.url
		item_dict['price_per_item'] = item.price_per_item
		ret_dict['item'].append(item_dict)

	return JsonResponse(ret_dict)
