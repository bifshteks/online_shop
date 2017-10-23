# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.base import TemplateView

from shop.models import Product

class Index(TemplateView):
	template_name = 'index2.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)

		context['products'] = Product.objects.all()

		return context


def about(request):
	return render(request, 'about.html')

def contacts(request):
	return render(request, 'contact-us.html')
	
