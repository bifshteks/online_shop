# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.base import TemplateView

from shop.models import Product, ItemsInCart
from blog.models import Posts
from main.models import Feedback
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

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

def search(request):
	req = [w.lower() for w in request.GET['s'].split()]
	items = Product.objects.filter(tags__name__in=req).distinct()
	posts = Posts.objects.filter(tags__name__in=req).distinct()
	session_key = request.session.session_key

	if not session_key:
		session_key = request.session.cycle_key()

	id_already_added_items = []
	all_user_ordered = [obj.item for obj in ItemsInCart.objects.filter(session_key=session_key, is_active=True)]
	for item in items:
		if item in all_user_ordered:
			id_already_added_items.append(int(item.id))


		

	context = {
		'items': items,
		'posts': posts,
		'search_request': ''.join(req),
		'list_of_added_items': id_already_added_items,
	}
	return render(request, 'search.html', context)
	
def feedback_ajax(request):
	data = request.POST
	name = data.get('cscf[name]')
	email = data.get('cscf[email]')
	message = data.get('cscf[message]')

	new_fb = Feedback.objects.create(name=name, email=email, message=message)
	new_fb.save()

	res_dict = dict()
	res_dict['errorlist'] = []

	if res_dict['errorlist']:
		res_dict['valid'] = False
	else:
		res_dict['valid'] = True


	try:
		subject = 'Новая заявка обратной связи с сайта calm-studio.ru'
		message = '''
		Информация по заявке:\n
		Имя: {}\n
		E-mail: {}\n
		Сообщение: {}
		'''.format(name, email, message)

		# sender = 'calm_studio@mail.ru'
		sender = 'whitenight.info@mail.ru'
		receiver = 'artem.pif@mail.ru'

		send_mail(
			subject,
			message,
			sender,
			[receiver],
			fail_silently=False
		)
		res_dict['sent'] = True
	except:
		res_dict['sent'] = False


	return JsonResponse(res_dict)