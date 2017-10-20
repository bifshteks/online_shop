# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Posts

def posts(request, page):
	posts = Posts.objects.all()
	range_slice = int(page) * 10
	returned_posts = posts[range_slice-10 : range_slice]
	context = {
		'posts': posts,
	}

	return render(request, 'posts.html', context)

def post(request, pk):
	post = Posts.objects.get(id=pk)

	context = {
		'post': post,
	}

	return render(request, 'post.html', context)

