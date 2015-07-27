from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
	url(r'^login/$', views.connection, name='connection'),
	)