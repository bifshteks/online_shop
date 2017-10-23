from django.conf.urls import url
import main.views as mv

urlpatterns = [
    url(r'^$', mv.Index.as_view(), name="index"),
    url(r'^abount/$', mv.about, name="about"),
    url(r'^contacts/$', mv.contacts, name="contacts"),
]