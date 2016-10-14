from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^form_submit$', views.submit),
	url(r'^success$', views.success)
]
