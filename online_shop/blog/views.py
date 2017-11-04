# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Posts

def posts(request):
	posts = Posts.objects.all().order_by('-id')[:5]
	# range_slice = int(page) * 10
	# returned_posts = posts[range_slice-10 : range_slice]
	context = {
		'posts': posts,
	}

	return render(request, 'blog.html', context)

def post(request, pk):
	post = Posts.objects.get(id=pk)

	context = {
		'post': post,
	}

	return render(request, 'blog-post.html', context)

