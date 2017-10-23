from django.conf.urls import url
import blog.views as bv

urlpatterns = [
	url(r'^$', bv.posts, name="blog"),
	url(r'^post/(?P<pk>\d+)/$', bv.post, name="post"),
	
]