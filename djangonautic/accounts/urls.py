from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    # url(r'^(?P<slug>[\w-]+)/$', views.details, name="details"),
]
