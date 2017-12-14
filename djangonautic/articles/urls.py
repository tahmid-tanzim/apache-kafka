from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.details, name="details"),
]
