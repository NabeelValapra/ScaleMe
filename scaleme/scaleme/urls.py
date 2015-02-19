from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogger import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogger/', include('blogger.urls', namespace='blogger')),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
