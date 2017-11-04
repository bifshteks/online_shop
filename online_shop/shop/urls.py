from django.conf.urls import url
import shop.views as sv

urlpatterns = [
	url(r'^catalog/$', sv.catalog, name="catalog_default"),
    url(r'^catalog/(?P<category>\D+)/$', sv.catalog, name="catalog"),
    url(r'^catalog/(?P<pk>\d+)/$', sv.item, name="item"),
    url(r'^cart/$', sv.cart, name="cart"),
    url(r'^cart_adding/$', sv.cart_adding_ajax, name="cart_adding"),
    url(r'^get_more_items/$', sv.get_more_items, name="get_more_items"),
    url(r'^get_more_catalog_items/$', sv.get_more_catalog_items, name="get_more_catalog_items"),
    url(r'^get_more_posts', sv.get_more_posts, name="get_more_posts"),
    url(r'^fix_order_in_cart/$', sv.fix_order_in_cart, name="fix_order_in_cart"),

]