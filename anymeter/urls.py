from django.conf.urls import patterns, include, url
from django.contrib import admin
from converter.api import v1_api
from converter import views

urlpatterns = patterns('',
	url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^chain/(?P<src_id>\d+)/(?P<trg_id>\d+)/$', views.chain),
)
