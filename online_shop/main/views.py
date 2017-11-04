# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.base import TemplateView

from shop.models import Product, ItemsInCart

class Index(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)

		items = Product.objects.order_by('-id')[:9]

		session_key = self.request.session.session_key

		if not session_key:
			session_key = self.request.session.cycle_key()

		id_already_added_items = []
		all_user_ordered = [obj.item for obj in ItemsInCart.objects.filter(session_key=session_key, is_active=True)]
		for item in items:
			if item in all_user_ordered:
				id_already_added_items.append(int(item.id))
		


		context['products'] = items
		context['list_of_added_items'] = id_already_added_items

		return context


def about(request):
	return render(request, 'about.html')

def contacts(request):
	return render(request, 'contacts.html')
	
