from django.conf.urls import url
import shop.views as sv

urlpatterns = [
    url(r'^catalog/$', sv.catalog, name="shop"),
    url(r'^catalog/(?P<pk>\d+)/$', sv.item, name="item"),
    url(r'^cart/$', sv.cart, name="cart"),
    url(r'^cart_adding/$', sv.cart_adding_ajax, name="cart_adding"),

]