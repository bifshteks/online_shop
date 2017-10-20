from django.conf.urls import url
import blog.views as bv

urlpatterns = [
	url(r'^(?P<page>\d+)/$', bv.posts, name="posts"),
	url(r'^article/(?P<pk>\d+)/$', bv.post, name="post"),
	
]