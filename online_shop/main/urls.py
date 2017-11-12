from django.conf.urls import url
import main.views as mv
from django.contrib.flatpages import views


urlpatterns = [
    url(r'^$', mv.Index.as_view(), name="index"),
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name="about"),
    url(r'^contacts/$', mv.contacts, name="contacts"),
    url(r'^search/$', mv.search, name="search"),
    url(r'^feedback_ajax/$', mv.feedback_ajax, name='feedback_ajax'),
]