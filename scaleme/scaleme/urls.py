from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blogger/', include('blogger.urls', namespace='blogger')),
    url(r'^optimj/', include('optimj.urls', namespace='optimj')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
