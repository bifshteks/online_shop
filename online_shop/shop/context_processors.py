from .models import ItemsInCart

def getting_cart_info(request):
	session_key = request.session.session_key
	if not session_key:
		session_key = request.session.cycle_key()

	items_in_cart = ItemsInCart.objects.filter(session_key=session_key, is_active=True)
	total_amount = items_in_cart.count()

	return locals()