from django.conf.urls import url
from blogger import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     url(r'^api/$',  views.api_root, name='api-root'),

    url(r'^blogs/$', views.BlogList.as_view(), name='blog-list'),
    url(r'^blogs/(?P<pk>[0-9]+)/$', views.BlogDetails.as_view(), name='blog-details'),

    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view(), name='user-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json',])
