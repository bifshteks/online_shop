from django.conf.urls import url
import main.views as mv

urlpatterns = [
    url(r'^$', mv.Index.as_view(), name="index"),
]