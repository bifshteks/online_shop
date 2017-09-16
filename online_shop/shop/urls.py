from django.conf.urls import url
import shop.views as sv

urlpatterns = [
    url(r'^catalog/(?P<page>\d+)/$', sv.catalog, name="catalog"),
    url(r'^catalog/item/(?P<pk>\d+)/$', sv.item, name="item"),
    url(r'^cart/$', sv.cart, name="cart"),
#   url(r'^order/$', sv.order, name="order"),
]