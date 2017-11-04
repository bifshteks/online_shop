# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from shop.models import Product
from django.http import JsonResponse
from .models import ItemsInCart, Product
from blog.models import Posts
from django.http import HttpResponse

def catalog(request, category='all'):
	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	id_already_added_items = []
	all_user_ordered = [obj.item for obj in ItemsInCart.objects.filter(session_key=session_key, is_active=True)]

	if category == 'handmade':
		items = Product.objects.filter(category__name='Авторские изделия').order_by('-id')[:9]
		for item in items:
			if item in all_user_ordered:
				id_already_added_items.append(int(item.id))
		category_name = 'Авторские изделия'
	elif category == 'china':
		items = Product.objects.filter(category__name='Товары из Китая').order_by('-id')[:9]
		for item in items:
			if item in all_user_ordered:
				id_already_added_items.append(int(item.id))
		category_name = 'Товары из Китая'
	elif category == 'build':
		items = Product.objects.filter(category__name='Строительные товары').order_by('-id')[:9]
		for item in items:
			if item in all_user_ordered:
				id_already_added_items.append(int(item.id))
		category_name = 'Строительные товары'
	else:
		# items = [obj for obj in Product.objects.order_by('-get_discount_price') if obj.price > obj.get_discount_price][:9]
		# items += [obj for obj in Product.objects.all() if obj.price == obj.get_discount_price][:9]
		# items = Product.objects.filter(price__gt=Func('get_discount_price')).order_by('-get_discount_price')[:9]
		# items += Product.objects.filter(price__e=F('get_discount_price'))
		
		unsorted = []
		items_wo_dis = []
		print('all i have', all_user_ordered)
		print()
		print('all that go into temp', id_already_added_items)
		
		# unsorted = [obj for obj in Product.objects.all() if obj.price > obj.get_discount_price()][:9]
		for obj in Product.objects.all():
			if obj.price > obj.get_discount_price():
				unsorted.append(obj)
			if obj in all_user_ordered:
				id_already_added_items.append(int(obj.id))
				print('YEEEAH')

			if len(unsorted) >= 9:
				break


		items = sorted(unsorted, key= lambda t: t.get_discount_price())
		for obj in Product.objects.all():
			if obj.price == obj.get_discount_price:
				items_wo_dis.append(obj)
			if obj in all_user_ordered:
				id_already_added_items.append(int(obj.id))

			if len(items_wo_dis) >= 9 - len(items):
				break
		# items += [obj for obj in Product.objects.all() if obj.price == obj.get_discount_price][:9 - len(unsorted)]
		items += items_wo_dis
		category_name = 'Все товары'



	context = {
		'items': items,
		'category_name': category_name,
		'list_of_added_items': id_already_added_items,
	}

	return render(request, 'shop.html', context)

def item(request, pk):
	# session_key = request.session.session_key

	# if not session_key:
	# 	session_key = request.session.cycle_key()

	item = Product.objects.get(id=pk)

	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	id_already_added_items = []
	all_user_ordered = [obj.item for obj in ItemsInCart.objects.filter(session_key=session_key, is_active=True)]

	if item in all_user_ordered:
		id_already_added_items.append(int(item.id))

	context = {
		'item': item,
		'list_of_added_items': id_already_added_items,
	}

	return render(request, 'item.html', context)

def cart(request):
	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	items = ItemsInCart.objects.filter(session_key=session_key, is_active=True)

	total_order_price = 0

	for item in items:
		total_order_price += item.total_price * item.amount

	context = {
		'items': items,
		'price_unch': total_order_price,

	}

	return render(request, 'cart.html', context)

def fix_order_in_cart(request):
	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	data = request.POST
	print(session_key)
	print(data.get('item_id'))
	item = ItemsInCart.objects.get(session_key=session_key, item__id=int(data.get('item_id')))
	item.amount = int(data.get('amount'))
	print(type(item.amount))
	if item.amount == 0:
		item.is_active = False
	else:
		item.is_active =  True
	item.save()

	return HttpResponse('')


def cart_adding_ajax(request):
	session_key = request.session.session_key

	# ret_dict = dict()


	data = request.POST
	item = Product.objects.get(id=int(data.get('item_id')))
	if data.get('amount'):
		amount = data.get('amount')
	else:
		amount = 1

	# new_order_in_cart, created = ItemsInCart.objects.get_or_create(session_key=session_key, item=items_id, defaults={'amount':amount})
	# if not created:
	# 	new_order_in_cart.amount += int(amount)
	# 	new_order_in_cart.save(force_update=True)
	new_order, created = ItemsInCart.objects.get_or_create(session_key=session_key, item=item, defaults={'amount':amount})
	if not created:
		new_order.is_active = True
		new_order.amount = amount
		new_order.save(force_update=True)
	print('SUCCSESSS')

	

	return HttpResponse('')

def get_more_items(request):
	'''Func for index list of items'''

	ret_dict = dict()
	data = request.POST


	items = Product.objects.filter(id__lt=data.get('last_id')).order_by('-id')[:9]

	first_el_in_db = Product.objects.all()[0]

	ret_dict['is_it_end'] = False

	if len(items) < 9 or first_el_in_db.id == items[8].id:
		ret_dict['is_it_end'] = True

	ret_dict['item'] = []


	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	id_already_added_items = []
	all_user_ordered = [obj.item for obj in ItemsInCart.objects.filter(session_key=session_key, is_active=True)]
	for item in items:
		if item in all_user_ordered:
			id_already_added_items.append(int(item.id))
	ret_dict['items_added'] = id_already_added_items

	for item in items:
		mid_dict = dict()
		mid_dict['price'] = item.price
		mid_dict['discount_price'] = item.get_discount_price()
		mid_dict['item_url'] = reverse('item', kwargs={'pk' : item.id})
		mid_dict['img_url'] = item.img1.url
		mid_dict['item_id'] = item.id
		mid_dict['title'] = item.title
		ret_dict['item'].append(mid_dict)



	return JsonResponse(ret_dict)

def get_more_catalog_items(request):
	'''Func for catalog list of items'''
	ret_dict = dict()
	data = request.POST
	ret_dict['is_it_end'] = False
	if data.get('category_name') != 'Все товары':

		category_name = data.get('category_name')

		items = Product.objects.filter(category__name=category_name, id__lt=data.get('last_id')).order_by('-id')[:9]
		first_el_in_db = Product.objects.filter(category__name=category_name)[0]
		if len(items) < 9 or first_el_in_db.id == items[8].id:
			ret_dict['is_it_end'] = True

	else:
		all_sorted_after_last_id = []
		items_without_dis = []
		# items = Product.objects.filter(id__lt=data.get('last_id'), price__gt=F('get_discount_price')).order_by('-get_discount_price')[:9]
		# items += Product.objects.filter(id__lt=data.get('last_id'), price__e=F('get_discount_price'))
		go_next = False
		go_next2 = True
		is_last_id_in_dis = False
		all_with_dis = [obj for obj in Product.objects.all() if obj.price > obj.get_discount_price()]
		all_with_dis = sorted(all_with_dis, key= lambda t: t.get_discount_price())
		all_without_dis = [obj for obj in Product.objects.all() if obj.price == obj.get_discount_price()]

		for obj in all_with_dis:
			if obj.id == int(data.get('last_id')):
				go_next = True
				is_last_id_in_dis = True
				continue
			if go_next:
				all_sorted_after_last_id.append(obj)
				if len(all_sorted_after_last_id) >= 9:
					go_next2 = False
					break
		# items = sorted(all_sorted_after_last_id, key= lambda t: t.get_discount_price())

		if go_next2:
			go_next2 = False
			for obj in [x for x in Product.objects.all() if x.price == x.get_discount_price()]:
				if is_last_id_in_dis:
					go_next2 = True
				if obj.id == int(data.get('last_id')):
					go_next2 = True
					continue
				if go_next2:
					items_without_dis.append(obj)
					if len(items_without_dis) >= 9:
						break
		items = all_sorted_after_last_id + items_without_dis
		

		# unsorted = [obj for obj in Product.objects.filter(id__gt=data.get('last_id')) if obj.price > obj.get_discount_price()][:9]
		# items += [obj for obj in Product.objects.filter(id__gt=data.get('last_id')) if obj.price == obj.get_discount_price][:9 - len(unsorted)]


		
		# sorted_all_dis = sorted(unsorted, key= lambda t: t.get_discount_price())
		all_sorted_by_dis = all_with_dis + all_without_dis

		last_el_in_db = all_sorted_by_dis[len(all_sorted_by_dis) - 1]


		if len(items) < 9 or last_el_in_db.id == items[8].id:
			ret_dict['is_it_end'] = True

	ret_dict['item'] = []

	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	id_already_added_items = []
	all_user_ordered = [obj.item for obj in ItemsInCart.objects.filter(session_key=session_key, is_active=True)]
	for item in items:
		if item in all_user_ordered:
			id_already_added_items.append(int(item.id))
	ret_dict['items_added'] = id_already_added_items



	for item in items:
		mid_dict = dict()
		mid_dict['price'] = item.price
		mid_dict['discount_price'] = item.get_discount_price()
		mid_dict['item_url'] = reverse('item', kwargs={'pk' : item.id})
		mid_dict['img_url'] = item.img1.url
		mid_dict['item_id'] = item.id
		mid_dict['title'] = item.title
		ret_dict['item'].append(mid_dict)


	return JsonResponse(ret_dict)

def get_more_posts(request):

	ret_dict = dict()
	data = request.POST

	all_last_item_id = Posts.objects.all()[0].id



	items = Posts.objects.filter(id__lt=int(data.get('last_id'))).order_by('-id')[:5]

	ret_dict['item'] = []

	ret_dict['is_it_last'] = False

	if len(items) < 5 or items[4].id == all_last_item_id:
		ret_dict['is_it_last'] = True



	for item in items:
		mid_dict = dict()
		mid_dict['post_url'] = reverse('item', kwargs={'pk' : item.id})
		mid_dict['img_url'] = item.img.url
		mid_dict['post_id'] = item.id
		mid_dict['post_title'] = item.title
		mid_dict['post_short_text'] = item.text[:460]
		ret_dict['item'].append(mid_dict)



	return JsonResponse(ret_dict)


