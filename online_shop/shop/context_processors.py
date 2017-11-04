from blog.models import Posts

def getting_cart_info(request):
	posts = Posts.objects.order_by('-id')[:5]
	context = {
		'recent_posts': posts,
	}

	return context